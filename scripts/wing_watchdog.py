#!/usr/bin/env python3
"""
WING Project Watchdog for huahua (mini2 OpenClaw)
监控 AIWH 项目中"处理中"的 ticket，检测任务悬停并自动提醒。
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
STALL_THRESHOLD_MINUTES = 60


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
    # status name in JQL must be English
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


def parse_jira_time(ts_str):
    ts_str = ts_str.replace("+0800", "+08:00")
    try:
        return datetime.fromisoformat(ts_str)
    except:
        return datetime.now(timezone.utc)


def write_alert(ticket_key, summary, stall_minutes, assignee, git_status):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert = f"""## 任务悬停提醒 [{ts}]

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

---
"""
    with open(ALERT_FILE, "a", encoding="utf-8") as f:
        f.write(alert + "\n")
    log(f"ALERT written for {ticket_key} (stall={stall_minutes}min)")


def main():
    log("=== WING Watchdog Start ===")
    tickets = get_in_progress_tickets()
    log(f"Found {len(tickets)} ticket(s) in '处理中' status")
    if not tickets:
        log("No stalled tickets. Exiting.")
        return

    git_status = check_git_status()
    log(f"Git status: {git_status}")

    now = datetime.now(timezone.utc)
    alerts_triggered = 0

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

    log(f"Alerts triggered: {alerts_triggered}")
    log("=== WING Watchdog End ===\n")


if __name__ == "__main__":
    main()
