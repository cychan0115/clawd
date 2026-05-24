# WING 项目任务执行流程 (huahua 专用)

## 任务生命周期

### 1. Claim Ticket
```bash
# 在 Jira 上设置 assignee 和状态
# 然后持久化任务状态
python3 ~/clawd/scripts/task_state_manager.py claim AIWH-XXX
```

### 2. 执行前检查 (Preflight Check)
```bash
# 检查当前任务状态
python3 ~/clawd/scripts/task_state_manager.py status
```

### 3. 执行任务
- 按 ticket 描述执行
- 定期更新 Jira 评论（超过 30 分钟）

### 4. 完成任务
```bash
# 代码提交
cd ~/workspace/wing_1
git add .
git commit -m "AIWH-XXX: done"
git push origin master

# 清除持久化状态
python3 ~/clawd/scripts/task_state_manager.py done AIWH-XXX

# 在 Jira 上提交 Done Report
# 将 ticket 状态改为"完成"
```

## Gateway 重启后的恢复

如果 OpenClaw gateway 重启了：

1. **自动检测**: 启动脚本会检查 `~/clawd/wing_current_task.json`
2. **恢复提醒**: 写入 `~/clawd/wing_recovery_alert.md`
3. **手动恢复**:
   ```bash
   # 查看恢复提醒
   cat ~/clawd/wing_recovery_alert.md
   
   # 检查任务状态
   python3 ~/clawd/scripts/task_state_manager.py status
   
   # 如已完成，执行收尾
   python3 ~/clawd/scripts/task_state_manager.py recover
   ```

## 关键文件

| 文件 | 用途 |
|------|------|
| `~/clawd/wing_current_task.json` | 当前执行的任务状态 |
| `~/clawd/wing_recovery_alert.md` | Gateway 重启后的恢复提醒 |
| `~/clawd/wing_watchdog_alerts.md` | Watchdog 检测到的悬停提醒 |
| `~/clawd/scripts/task_state_manager.py` | 任务状态管理工具 |
| `~/clawd/scripts/wing_watchdog_v2.py` | 监控脚本 |

## 规则

1. **Claim 时必须持久化** — 运行 `task_state_manager.py claim`
2. **Done 时必须清除** — 运行 `task_state_manager.py done`
3. **重启后检查恢复提醒** — 读取 `wing_recovery_alert.md`
4. **不要同时执行多个 ticket** — 一次一票
