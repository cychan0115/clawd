#!/usr/bin/env python3
"""Jira自动化任务处理器 - 用于cron执行"""

import requests
import subprocess
import json
import sys
import os
from datetime import datetime

# 配置
JIRA_BASE = "https://3pigc.atlassian.net"
# Token 从环境变量读取，避免硬编码提交到仓库
TOKEN = os.environ.get("JIRA_API_TOKEN", "")
if not TOKEN:
    raise RuntimeError("请设置环境变量 JIRA_API_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}
ACCOUNT_ID = "772751111025"  # 从token中解析

WORKSPACE = "/Users/3pigcn/clawd"

def jira_get(path):
    url = f"{JIRA_BASE}{path}"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json()

def jira_post(path, data):
    url = f"{JIRA_BASE}{path}"
    resp = requests.post(url, headers=HEADERS, json=data, timeout=30)
    resp.raise_for_status()
    return resp.json()

def jira_put(path, data):
    url = f"{JIRA_BASE}{path}"
    resp = requests.put(url, headers=HEADERS, json=data, timeout=30)
    resp.raise_for_status()
    return resp.json()

def run_cmd(cmd, cwd=None):
    """执行shell命令，返回 (returncode, stdout, stderr)"""
    result = subprocess.run(
        cmd, shell=True, cwd=cwd or WORKSPACE,
        capture_output=True, text=True, timeout=60
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def search_issues(jql):
    """搜索Jira issues"""
    url = f"{JIRA_BASE}/rest/api/2/search"
    params = {"jql": jql, "fields": "summary,status,assignee,description,comment", "maxResults": 50}
    resp = requests.get(url, headers=HEADERS, params=params, timeout=30)
    resp.raise_for_status()
    return resp.json().get("issues", [])

def add_comment(issue_key, body):
    """添加comment"""
    jira_post(f"/rest/api/2/issue/{issue_key}/comment", {"body": body})

def transition_issue(issue_key, transition_id):
    """转换状态"""
    jira_post(f"/rest/api/2/issue/{issue_key}/transitions", {
        "transition": {"id": transition_id}
    })

def assign_issue(issue_key, account_id):
    """Assign issue"""
    jira_put(f"/rest/api/2/issue/{issue_key}/assignee", {"accountId": account_id})

def get_git_status():
    """获取git状态"""
    rc, out, err = run_cmd("git status --short")
    return out, rc

def get_git_log():
    """获取最近commit"""
    rc, out, err = run_cmd("git log -1 --oneline")
    return out, rc

def git_push():
    """执行git push"""
    rc, out, err = run_cmd("git push origin master")
    return rc == 0, out, err

def git_commit_and_push(message):
    """执行git add, commit, push"""
    run_cmd("git add .")
    rc, out, err = run_cmd(f'git commit -m "{message}"')
    if rc == 0:
        rc2, out2, err2 = run_cmd("git push origin master")
        return rc2 == 0, out2, err2
    return False, out, err

def main():
    print("=" * 60)
    print(f"[Jira Task Processor] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Step 1: 检查"处理中"的ticket
    print("\n[Step 1] 检查'处理中'的ticket...")
    in_progress = search_issues(
        'project = AIWH AND status = "处理中" AND assignee = currentUser()'
    )
    print(f"  Found {len(in_progress)} in-progress ticket(s)")

    if in_progress:
        issue = in_progress[0]  # 一次处理一个
        key = issue["key"]
        fields = issue["fields"]
        summary = fields.get("summary", "")
        print(f"  Processing: {key} - {summary}")

        # 检查git状态
        git_status, _ = get_git_status()
        print(f"  Git status: {git_status[:200] if git_status else 'clean'}")

        if git_status:
            # 有未提交的代码，尝试commit和push
            print("  -> 检测到未提交代码，执行 commit + push...")
            success, out, err = git_commit_and_push(f"{key}: {summary}")
            if success:
                commit, _ = get_git_log()
                done_report = f"""[Done Report]

任务已完成，代码已提交。

- Commit: {commit}
- Git Output: {out}

Status: READY FOR REVIEW
"""
                add_comment(key, done_report)
                transition_issue(key, "41")
                run_cmd(f"python3 ~/clawd/scripts/task_state_manager.py done {key}")
                print(f"  -> {key} 已标记为完成")
            else:
                blocker = f"""[BLOCKER]

Git操作失败:
- stdout: {out}
- stderr: {err}

需要手动处理未提交的代码。
"""
                add_comment(key, blocker)
                print(f"  -> {key} 遇到Git错误，已写BLOCKER")
        else:
            # 检查是否有未push的commit
            rc, ahead, _ = run_cmd("git log origin/master..HEAD --oneline")
            if ahead:
                print("  -> 检测到未push的commit，执行 push...")
                success, out, err = git_push()
                if success:
                    commit, _ = get_git_log()
                    done_report = f"""[Done Report]

代码已push到远程。

- Commit: {commit}
- Push Output: {out}

Status: READY FOR REVIEW
"""
                    add_comment(key, done_report)
                    transition_issue(key, "41")
                    run_cmd(f"python3 ~/clawd/scripts/task_state_manager.py done {key}")
                    print(f"  -> {key} 已标记为完成")
                else:
                    blocker = f"""[BLOCKER]

Push失败:
- stderr: {err}

需要手动处理。
"""
                    add_comment(key, blocker)
            else:
                # 没有代码修改，写BLOCKER
                blocker = f"""[BLOCKER]

任务状态为"处理中"但本地没有代码修改或待push的commit。

- Git status: clean
- 没有检测到工作内容

请确认是否遗漏了代码修改，或需要重新规划任务。
"""
                add_comment(key, blocker)
                print(f"  -> {key} 没有代码修改，已写BLOCKER")

        return  # 先处理完"处理中"的，再处理下一个cron周期

    # Step 2: 检查待领取的ticket
    print("\n[Step 2] 检查'Selected for Development'的ticket...")
    todo = search_issues(
        'project = AIWH AND status = "Selected for Development" AND assignee is EMPTY'
    )
    print(f"  Found {len(todo)} available ticket(s)")

    if not todo:
        print("\n[Result] 当前没有待处理的Jira任务。")
        return

    # 领取第一个ticket
    issue = todo[0]
    key = issue["key"]
    fields = issue["fields"]
    summary = fields.get("summary", "")
    description = fields.get("description", "")
    print(f"  Claiming: {key} - {summary}")

    # Assign给自己
    assign_issue(key, "772751111025")
    print(f"  -> 已assign给huahua")

    # 转换到"处理中"
    transition_issue(key, "31")
    print(f"  -> 状态已改为'处理中'")

    # 写Preflight Check
    preflight = f"""[Preflight Check]

已领取任务，准备执行。

- Ticket: {key}
- Summary: {summary}
- Description: {description[:500] if description else 'N/A'}

下一步：读取任务要求并执行。
"""
    add_comment(key, preflight)
    print(f"  -> 已写Preflight Check")

    # 更新任务状态管理器
    run_cmd(f"python3 ~/clawd/scripts/task_state_manager.py claim {key}")
    print(f"  -> 已更新任务状态")

    # 读取ticket详情（已经在fields中）
    print(f"\n[Ticket Details] {key}")
    print(f"  Summary: {summary}")
    print(f"  Description: {description}")

    # 这里需要执行任务。由于任务类型多样，
    # 我们输出任务信息，由调用者决定如何执行。
    print(f"\n[Action Required] 需要执行ticket: {key}")
    print(f"  请根据任务描述执行具体工作，然后:")
    print(f"  1. git add . && git commit -m '{key}: {summary}' && git push origin master")
    print(f"  2. 写Done Report comment")
    print(f"  3. transition到'完成' (id 41)")
    print(f"  4. 运行 task_state_manager.py done {key}")

    # 将任务信息写入文件，供后续处理
    task_info = {
        "key": key,
        "summary": summary,
        "description": description,
        "claimed_at": datetime.now().isoformat()
    }
    with open(f"{WORKSPACE}/.current_jira_task.json", "w") as f:
        json.dump(task_info, f, indent=2, ensure_ascii=False)
    print(f"  -> 任务信息已保存到 .current_jira_task.json")

    # 返回任务信息，让外部可以继续执行
    print(f"\n{'='*60}")
    print(f"[CLAIMED] {key}: {summary}")
    print(f"{'='*60}")
    return key, summary, description

if __name__ == "__main__":
    result = main()
    if isinstance(result, tuple):
        key, summary, desc = result
        # 输出JSON格式的任务信息，方便解析
        print("\n---TASK_INFO---")
        print(json.dumps({"key": key, "summary": summary, "description": desc}, ensure_ascii=False))
