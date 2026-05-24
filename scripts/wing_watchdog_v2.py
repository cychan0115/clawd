#!/usr/bin/env python3
"""
WING Project Watchdog v2 for huahua (mini2 OpenClaw)
监控 AIWH 项目中"处理中"的 ticket，检测任务悬停并自动提醒/唤醒。

新增功能:
1. 检测 gateway 重启后的任务恢复
2. 尝试通过 Jira 评论"唤醒" huahua
3. 读取 task_state_manager 的持久化状态
"""

import os
import json
import subprocess
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

JIRA_URL = "http://116.205.141.57:50008"
TOKEN = "<BB_TOKEN_REDACTED>"
PROJECT_KEY = "AIWH"
WORKSPACE_DIR = Path.home() / "workspace" / "wing_1"
ALERT_FILE = Path.home() / "clawd" / "wing_watchdog_alerts.md"
LOG_FILE = Path.home() / "clawd" / "wing_watchdog.log"
RECOVERY_FILE = Path.home() / "clawd" / "wing_recovery_alert.md"
STATE_FILE = Path.home() / "clawd" / "wing_current_task.json"
STALL_THRESHOLD_MINUTES = 60
WAKEUP_THRESHOLD_MINUTES = 30  # 30分钟就开始尝试唤醒


def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def jira_api(path, method="GET", data=None):
    url = f"{JIRA_URL}{path}"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }
    if data:
        data = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read()
            if body:
                return json.loads(body), resp.status
            return {}, resp.status
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        return {"error": err_body, "status": e.code}, e.code


def get_in_progress_tickets():
    jql = 'project=AIWH AND status="In Progress" ORDER BY updated ASC'
    encoded_jql = quote(jql)
    result, status = jira_api(f"/rest/api/2/search?jql={encoded_jql}&maxResults=20")
    if status != 200:
        log(f"ERROR: Failed to search Jira tickets: {result.get('error', 'unknown')}")
        return []
    return result.get("issues", [])


def check_git_status():
    if not WORKSPACE_DIR.exists():
        return None
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=WORKSPACE_DIR,
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode != 0:
            return f"git error: {result.stderr.strip()}"
        lines = [l for l in result.stdout.strip().split("\n") if l.strip()]
        if not lines:
            return "clean"
        untracked = sum(1 for l in lines if l.startswith("?"))
        modified = sum(1 for l in lines if l.startswith(" M") or l.startswith("M "))
        return f"untracked={untracked}, modified={modified}"
    except Exception as e:
        return f"exception: {e}"


def read_persisted_state():
    if not STATE_FILE.exists():
        return None
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        log(f"ERROR reading persisted state: {e}")
        return None


def parse_jira_time(ts_str):
    ts_str = ts_str.replace("+0800", "+08:00")
    try:
        return datetime.fromisoformat(ts_str)
    except:
        return datetime.now(timezone.utc)


def write_alert(ticket_key, summary, stall_minutes, assignee, git_status, reason="stall"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert = f"""## 任务{"悬停" if reason == "stall" else "恢复"}提醒 [{ts}]

**Ticket**: [{ticket_key}]({JIRA_URL}/browse/{ticket_key})
**标题**: {summary}
**Assignee**: {assignee}
**悬停时间**: {stall_minutes} 分钟

### 检测到的问题
- Jira 状态为"处理中"，但已 {stall_minutes} 分钟无更新
- 本地 Git 状态: `{git_status}`

### 建议行动
1. 检查代码是否已完成但未 commit/push
2. 如果已完成，执行:
   ```bash
   cd ~/workspace/wing_1
   git add .
   git commit -m "{ticket_key}: done"
   git push origin master
   ```
3. 在 Jira 上提交 [Done Report]
4. 将 ticket 状态改为"完成"
5. 运行: `python3 ~/clawd/scripts/task_state_manager.py done {ticket_key}`

---
"""
    with open(ALERT_FILE, "a", encoding="utf-8") as f:
        f.write(alert + "\n")
    log(f"ALERT written for {ticket_key} (stall={stall_minutes}min)")


def send_wakeup_comment(ticket_key, stall_minutes, git_status):
    """通过 Jira 评论尝试唤醒 huahua"""
    comment_body = f"""## [WATCHDOG WAKEUP] {ticket_key}

**时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} CST
**悬停**: {stall_minutes} 分钟

### huahua 请立即检查此任务
- 本地 Git 状态: `{git_status}`
- 如代码已完成，请执行 commit/push/Done Report
- 如遇到 BLOCKER，请在此评论说明

### 快捷命令
```bash
cd ~/workspace/wing_1
git status
git add . && git commit -m "{ticket_key}: done" && git push origin master
```

---
*此评论由 WING Watchdog 自动发送*
"""
    result, status = jira_api(f"/rest/api/2/issue/{ticket_key}/comment", method="POST", data={"body": comment_body})
    if status == 201:
        log(f"WAKEUP comment sent for {ticket_key}")
        return True
    else:
        log(f"WAKEUP comment failed for {ticket_key}: {result.get('error', 'unknown')}")
        return False


def check_recovery():
    """检查 gateway 重启后的任务恢复"""
    state = read_persisted_state()
    if not state:
        return

    ticket_key = state.get("ticket_key")
    claimed_at = state.get("claimed_at")
    log(f"RECOVERY CHECK: Found persisted state for {ticket_key} (claimed at {claimed_at})")

    # Check if ticket is still in progress
    issue, status = jira_api(f"/rest/api/2/issue/{ticket_key}")
    if status != 200:
        log(f"RECOVERY CHECK: Failed to fetch {ticket_key}")
        return

    issue_status = issue["fields"]["status"]["name"]
    if issue_status != "处理中":
        log(f"RECOVERY CHECK: {ticket_key} status is {issue_status}, not In Progress. Clearing state.")
        STATE_FILE.unlink(missing_ok=True)
        return

    # Ticket still in progress, write recovery alert
    git_status = check_git_status()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert = f"""## Gateway 重启后任务恢复提醒 [{ts}]

**Ticket**: [{ticket_key}]({JIRA_URL}/browse/{ticket_key})
**原始 Claim 时间**: {claimed_at}
**当前 Git 状态**: `{git_status}`

### Gateway 已重启，此任务可能未完成
1. 检查代码状态
2. 如已完成: commit/push/Done Report
3. 运行: `python3 ~/clawd/scripts/task_state_manager.py done {ticket_key}`

---
"""
    with open(RECOVERY_FILE, "a", encoding="utf-8") as f:
        f.write(alert + "\n")
    log(f"RECOVERY alert written for {ticket_key}")


def main():
    log("=== WING Watchdog v2 Start ===")

    # 1. Check for recovery after gateway restart
    check_recovery()

    # 2. Get in-progress tickets
    tickets = get_in_progress_tickets()
    log(f"Found {len(tickets)} ticket(s) in '处理中' status")
    if not tickets:
        log("No stalled tickets. Exiting.")
        return

    git_status = check_git_status()
    log(f"Git status: {git_status}")

    now = datetime.now(timezone.utc)
    alerts_triggered = 0
    wakeups_sent = 0

    for issue in tickets:
        key = issue["key"]
        fields = issue["fields"]
        summary = fields["summary"]
        updated_str = fields["updated"]
        assignee = fields.get("assignee", {})
        assignee_name = assignee.get("displayName", "Unassigned") if assignee else "Unassigned"

        updated = parse_jira_time(updated_str)
        stall_minutes = int((now - updated).total_seconds() / 60)
        log(f"{key}: updated={updated_str}, stall={stall_minutes}min, assignee={assignee_name}")

        if stall_minutes >= STALL_THRESHOLD_MINUTES:
            write_alert(key, summary, stall_minutes, assignee_name, git_status)
            alerts_triggered += 1

        # Try wakeup at 30 minutes
        if stall_minutes >= WAKEUP_THRESHOLD_MINUTES and stall_minutes < STALL_THRESHOLD_MINUTES:
            if send_wakeup_comment(key, stall_minutes, git_status):
                wakeups_sent += 1

    log(f"Alerts triggered: {alerts_triggered}, Wakeups sent: {wakeups_sent}")
    log("=== WING Watchdog v2 End ===\n")


if __name__ == "__main__":
    main()
