# WING 项目自检流程

每次 huahua 启动或恢复连接时，执行以下检查：

## 1. 读取 Watchdog Alert 文件

```bash
cat ~/clawd/wing_watchdog_alerts.md 2>/dev/null || echo "无悬停提醒"
```

## 2. 如果有 Alert，按优先级处理

1. **检查本地 Git 状态**
   ```bash
   cd ~/workspace/wing_1 && git status
   ```

2. **如有未提交代码**
   - 确认代码已完成
   - `git add . && git commit -m "TICKET-KEY: done"`
   - `git push origin master`

3. **在 Jira 上提交 Done Report**
   - 按模板填写验收清单
   - 附上 commit hash 或文件清单

4. **将 ticket 状态改为"完成"**

5. **清理 Alert 文件**
   ```bash
   rm ~/clawd/wing_watchdog_alerts.md
   ```

## 3. 检查 Jira 中"处理中"的 ticket

- 确认当前是否有自己负责的在处理中 ticket
- 确认没有遗漏的 Done Report

## 4. 无 Alert 时的正常流程

- 继续处理当前 ticket
- 或从 Backlog 领取新 ticket

---

*此 skill 由 Anna 部署，用于防止任务悬停*
