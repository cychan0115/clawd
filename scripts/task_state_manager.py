#!/usr/bin/env python3
"""
WING Task State Manager for huahua (mini2 OpenClaw)
持久化当前执行的任务状态，gateway 重启后可恢复上下文。

用法:
  python3 task_state_manager.py claim AIWH-99
  python3 task_state_manager.py done AIWH-99
  python3 task_state_manager.py status
  python3 task_state_manager.py recover
"""

import os
import sys
import json
from datetime import datetime, timezone
from pathlib import Path

STATE_FILE = Path.home() / "clawd" / "wing_current_task.json"
LOG_FILE = Path.home() / "clawd" / "wing_task_state.log"


def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def read_state():
    if not STATE_FILE.exists():
        return None
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        log(f"ERROR reading state: {e}")
        return None


def write_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    log(f"State written: {state}")


def clear_state():
    if STATE_FILE.exists():
        STATE_FILE.unlink()
        log("State cleared")


def cmd_claim(ticket_key):
    state = {
        "ticket_key": ticket_key,
        "status": "in_progress",
        "claimed_at": datetime.now(timezone.utc).isoformat(),
        "workspace": str(Path.home() / "workspace" / "wing_1"),
    }
    write_state(state)
    print(f"Claimed {ticket_key}. State persisted.")


def cmd_done(ticket_key):
    state = read_state()
    if state and state.get("ticket_key") == ticket_key:
        clear_state()
        print(f"Marked {ticket_key} as done. State cleared.")
    else:
        log(f"WARNING: done called for {ticket_key} but current state is {state}")
        print(f"WARNING: No matching state found for {ticket_key}")


def cmd_status():
    state = read_state()
    if state:
        print(f"Current task: {state['ticket_key']}")
        print(f"Status: {state['status']}")
        print(f"Claimed at: {state['claimed_at']}")
        print(f"Workspace: {state['workspace']}")
    else:
        print("No active task.")


def cmd_recover():
    """Gateway 重启后调用，检查是否有未完成的任务"""
    state = read_state()
    if not state:
        print("No task to recover.")
        return

    ticket_key = state["ticket_key"]
    claimed_at = state["claimed_at"]
    workspace = state["workspace"]

    # Check if workspace has uncommitted changes
    import subprocess
    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=workspace,
            capture_output=True,
            text=True,
            timeout=10,
        )
        git_status = result.stdout.strip() if result.returncode == 0 else "error"
    except Exception as e:
        git_status = f"exception: {e}"

    recovery_info = {
        "ticket_key": ticket_key,
        "claimed_at": claimed_at,
        "workspace": workspace,
        "git_status": git_status,
        "recovered_at": datetime.now(timezone.utc).isoformat(),
    }

    # Write recovery alert
    alert_file = Path.home() / "clawd" / "wing_recovery_alert.md"
    alert = f"""## 任务恢复提醒 [{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]

**Ticket**: {ticket_key}
**原始 Claim 时间**: {claimed_at}
**Workspace**: {workspace}
**Git 状态**:
```
{git_status}
```

### Gateway 已重启，请检查此任务是否已完成
1. 如果已完成但未提交:
   ```bash
   cd {workspace}
   git add .
   git commit -m "{ticket_key}: done"
   git push origin master
   ```
2. 提交 [Done Report] 到 Jira
3. 将 ticket 状态改为"完成"
4. 运行: `python3 ~/clawd/scripts/task_state_manager.py done {ticket_key}`

---
"""
    with open(alert_file, "a", encoding="utf-8") as f:
        f.write(alert + "\n")

    log(f"Recovery alert written for {ticket_key}")
    print(f"Recovery alert written for {ticket_key}")
    print(f"Git status: {git_status}")


def main():
    if len(sys.argv) < 2:
        print("Usage: task_state_manager.py <claim|done|status|recover> [ticket_key]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "claim":
        if len(sys.argv) < 3:
            print("Usage: task_state_manager.py claim <ticket_key>")
            sys.exit(1)
        cmd_claim(sys.argv[2])
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Usage: task_state_manager.py done <ticket_key>")
            sys.exit(1)
        cmd_done(sys.argv[2])
    elif cmd == "status":
        cmd_status()
    elif cmd == "recover":
        cmd_recover()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
