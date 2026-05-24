#!/usr/bin/env python3
"""
WING Auto-Save for huahua (mini2 OpenClaw)
每 30 分钟自动 git commit，保存工作进度。
不 push，只 commit，避免冲突。

部署: crontab -e
*/30 * * * * cd ~/workspace/wing_1 && python3 ~/clawd/scripts/auto_save.py >> ~/clawd/auto_save.log 2>&1
"""

import os
import subprocess
from datetime import datetime
from pathlib import Path

WORKSPACE = Path.home() / "workspace" / "wing_1"
LOG_FILE = Path.home() / "clawd" / "auto_save.log"
TASK_STATE = Path.home() / "clawd" / "wing_current_task.json"


def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def get_current_ticket():
    """读取当前任务状态"""
    import json
    if not TASK_STATE.exists():
        return None
    try:
        with open(TASK_STATE, "r", encoding="utf-8") as f:
            state = json.load(f)
        return state.get("ticket_key")
    except Exception as e:
        log(f"ERROR reading task state: {e}")
        return None


def has_changes():
    """检查是否有未提交的更改"""
    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=WORKSPACE,
        capture_output=True,
        text=True,
        timeout=10,
    )
    if result.returncode != 0:
        log(f"git status error: {result.stderr.strip()}")
        return False
    return bool(result.stdout.strip())


def auto_commit(ticket_key):
    """自动 commit 当前更改"""
    # Configure git user if not set
    subprocess.run(
        ["git", "config", "user.email", "huahua@3pigc.com"],
        cwd=WORKSPACE,
        capture_output=True,
        timeout=5,
    )
    subprocess.run(
        ["git", "config", "user.name", "huahua"],
        cwd=WORKSPACE,
        capture_output=True,
        timeout=5,
    )

    # Add all changes
    result = subprocess.run(
        ["git", "add", "."],
        cwd=WORKSPACE,
        capture_output=True,
        text=True,
        timeout=10,
    )
    if result.returncode != 0:
        log(f"git add error: {result.stderr.strip()}")
        return False

    # Commit with auto message
    commit_msg = f"[{ticket_key}] auto-save at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    result = subprocess.run(
        ["git", "commit", "-m", commit_msg],
        cwd=WORKSPACE,
        capture_output=True,
        text=True,
        timeout=10,
    )
    if result.returncode != 0:
        # Might be nothing to commit
        if "nothing to commit" in result.stdout.lower() or "nothing to commit" in result.stderr.lower():
            log("Nothing to commit")
            return False
        log(f"git commit error: {result.stderr.strip()}")
        return False

    log(f"Auto-committed: {commit_msg}")
    
    # Push to remote
    result = subprocess.run(
        ["git", "push", "origin", "master"],
        cwd=WORKSPACE,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        log(f"git push error: {result.stderr.strip()}")
        return False
    
    log("Auto-pushed to origin/master")
    return True


def main():
    log("=== Auto-Save Start ===")

    # Check if workspace exists
    if not WORKSPACE.exists():
        log("Workspace not found, exiting")
        return

    # Get current ticket
    ticket = get_current_ticket()
    if not ticket:
        log("No active ticket, skipping auto-save")
        return

    log(f"Active ticket: {ticket}")

    # Check if there are changes
    if not has_changes():
        log("No changes to save")
        return

    # Auto commit
    if auto_commit(ticket):
        log("Auto-save successful")
    else:
        log("Auto-save skipped or failed")

    log("=== Auto-Save End ===\n")


if __name__ == "__main__":
    main()
