# Jira 巡查 BLOCKER — 2026-06-19 04:16 CST

## 状态
Jira Cloud 实例 **不可用**，无法执行 ticket 巡查。

## 错误详情
- 端点: `https://aiwriterhub.atlassian.net/rest/api/2/search`
- 返回: `{"errorMessage": "Site temporarily unavailable", "errorCode": "OTHER"}` (HTTP 404)
- 尝试的域名: aiwriterhub.atlassian.net, 3pigc.atlassian.net
- 尝试的 API 版本: api/2, api/3
- Atlassian 状态页面: 无全局故障报告

## 影响
- 无法查询"处理中"的 ticket
- 无法查询待领取的 ticket
- 无法 claim/transition/comment 任何 ticket

## 后续行动
- 等待 Jira Cloud 恢复后重试
- 建议 Anna 检查 Jira 实例状态或联系 Atlassian 支持
- 本次 cron 巡查跳过，下次心跳/cron 自动重试

## Evidence
```
Request ID: 12d10b5f86584c5bbd4f781539bde87a
Error: {"errorMessage": "Site temporarily unavailable", "errorCode": "OTHER"}
```
