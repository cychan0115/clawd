# Wing Recovery Alert

此文件用于 Gateway 重启后恢复任务上下文。

## 检查时间

- **最后更新**: 2026-07-01 09:44 CST
- **Agent**: huahua (mini2)

## 当前任务状态

- **活跃任务**: 无
- `task_state_manager.py status`: `No active task.`

## 恢复检查清单

Gateway 重启后，执行以下检查：

1. [ ] 运行 `python3 ~/clawd/scripts/task_state_manager.py status` 确认活跃任务
2. [ ] 如有活跃任务，运行 `python3 ~/clawd/scripts/task_state_manager.py recover`
3. [ ] 检查对应 workspace 的 git status
4. [ ] 如有未提交变更，立即 commit + push
5. [ ] 恢复 Jira 任务流转（如有）

---

*此文件由 task_state_manager.py recover 自动生成，无任务时为空模板。*
