#!/bin/bash
# WING Recovery on Startup
# 此脚本应在 OpenClaw gateway 启动后执行
# 检查是否有未完成的 WING 任务，并生成恢复提醒

echo "[$(date '+%Y-%m-%d %H:%M:%S')] WING Recovery on Startup"

# Check if there is a persisted task state
if [ -f "$HOME/clawd/wing_current_task.json" ]; then
    echo "Found persisted task state:"
    cat "$HOME/clawd/wing_current_task.json"
    echo ""
    
    # Run recovery check
    python3 "$HOME/clawd/scripts/task_state_manager.py" recover
    
    echo "Recovery alert written to $HOME/clawd/wing_recovery_alert.md"
else
    echo "No persisted task state found."
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] WING Recovery done"
