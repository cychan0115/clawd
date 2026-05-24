# Jira Cron Blocker Report — 2026-05-17 20:31

## Cron ID
`8d0227c6-23ec-434c-802a-97bdb590dc1f`

## 时间
2026-05-17 20:31 (Asia/Shanghai) / 2026-05-17 12:31 UTC

## 状态
❌ **BLOCKER: Jira API 认证持续失效**

## 详细验证

### 凭据来源
- `~/.openclaw/openclaw.json` → `skills.atlassian-jira-by-altf1be.env.JIRA_API_TOKEN` = `<JIRA_SECRET_REDACTED>`
- 备选凭据：`<JIRA_TOKEN_REDACTED>`
- 技能目录 `.env` 文件：已不存在（目录已被移除）

### 测试结果

| 端点 | 认证方式 | 结果 |
|---|---|---|
| `GET /rest/api/2/myself` | Bearer `<JIRA_SECRET_REDACTED>` | **401** — Client must be authenticated |
| `GET /rest/api/2/myself` | Basic Auth (`openclaw-admin` + old token) | **403** — AUTHENTICATION_DENIED |
| `GET /rest/api/2/project` | Bearer `<JIRA_SECRET_REDACTED>` | **200** `[]`（空数组，与无认证结果相同） |
| `GET /rest/api/2/project` | Basic Auth | **403** HTML |
| `GET /rest/api/2/project` | 无认证 | **200** `[]`（确认该端点无需认证） |
| `GET /rest/api/2/mypermissions` | Bearer `<JIRA_SECRET_REDACTED>` | **401** |
| `GET /rest/api/2/serverInfo` | 无需认证 | **200** ✅（Jira 9.4.0 Server 在线） |
| `GET /rest/api/2/project/AIWH` | Bearer `<JIRA_SECRET_REDACTED>` | **404** — 项目不存在或无权访问 |
| `GET /rest/api/2/search?jql=...` | Bearer `<JIRA_SECRET_REDACTED>` | **400** — 匿名用户无权查看 |

### 关键结论
1. **Jira 实例在线**（`serverInfo` 返回 9.4.0 Server）
2. **所有已知 API Token 均无法通过认证**（401/403）
3. **Bearer token 在任何需要认证的端点都失败**
4. **项目 AIWH 无法通过 API 访问**（404 或权限不足）
5. **baseUrl 实际为 `hw4.3pigcn.com:50008`**（API 显示），外部 IP `116.205.141.57:50008` 为同一实例

## 影响
- ❌ 无法查询 AIWH 项目 ticket
- ❌ 无法领取/更新/评论任何 ticket
- ❌ 全自动任务处理流程完全阻塞

## 与此前报告的对比
这是今天第 **5 轮** cron 验证（此前：18:36, 18:44, 19:04, 19:26, 20:11, 20:31），问题**持续未恢复**。

## 下一步
需要 Anna/CY 提供新的有效 Jira API Token，或：
1. 确认正确的 Jira 用户名 + API Token 组合
2. 检查 `openclaw-admin` 账户在 Jira 中的权限是否被撤销
3. 确认 AIWH 项目是否仍然存在且对该账户可见

## Evidence
- 本轮测试脚本完整输出保留在 cron log 中
- 此前 blocker 报告：`jira_cron_blocker_2026-05-17.md`（18:44）
- 此前 blocker 报告：`jira_cron_blocker_2026-05-17_1904.md`（19:04）
- 此前 blocker 报告：`jira_cron_blocker_2026-05-17_1926.md`（19:26）
- 此前 blocker 报告：`jira_cron_blocker_2026-05-17_2011.md`（20:11）
