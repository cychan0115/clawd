# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

## WING Project Task Check

每次心跳或会话恢复时，执行以下检查：

1. **检查未完成任务状态**
   ```bash
   python3 ~/clawd/scripts/task_state_manager.py status
   ```

2. **如果有未完成任务**
   - 读取 `~/clawd/wing_recovery_alert.md` 了解详情
   - 检查本地 Git 状态
   - 如代码已完成：commit/push/Done Report
   - 运行 `task_state_manager.py done TICKET-KEY` 清除状态

3. **检查悬停提醒**
   ```bash
   cat ~/clawd/wing_watchdog_alerts.md 2>/dev/null || echo "无悬停提醒"
   ```

## 规则

- 发现未完成任务时，优先处理，不要忽略
- Gateway 重启后，务必执行恢复检查
- 一次只处理一个 ticket
