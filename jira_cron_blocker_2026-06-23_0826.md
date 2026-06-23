# Jira 巡查 BLOCKER 报告 - 2026-06-23 08:26

**时间**: 2026-06-23 08:26 CST (Tuesday)  
**触发**: cron 任务巡查（优化版流程）  
**Agent**: huahua  
**状态**: 🔴 BLOCKED — Jira 双实例不可用

---

## 问题摘要

本次巡查发现 Jira **双实例全部不可用**，无法执行任何 ticket 查询或操作。

---

## Jira Cloud (主站)

- **URL**: `https://3pigc.atlassian.net`
- **状态**: ❌ HTTP 404 — 持续不可用
- **持续时长**: 自 2026-06-16 23:45 CST 起，已约 **~149 小时**（~6.2 天）
- **Atlassian 状态页**: 显示 All Systems Operational，但实例级别不可用

---

## Jira Data Center (备用)

- **URL**: `http://116.205.141.57:50008` / `http://hw4.3pigcn.com:50008`
- **Jira 版本**: 9.4.0 Server (build 940000, 2022-11-14)
- **HTTP 状态**: ✅ 200（服务本身在运行）
- **认证状态**: ❌ **全部失败** — 所有请求返回 `X-AUSERNAME: anonymous`
- **测试方式**:
  - Bearer Token: `Authorization: Bearer [JIRA_TOKEN_TRUNCATED]` → anonymous
  - Basic Auth (email:token): `huahua@3pigc.com:token` → 空响应
  - Basic Auth (user:token): `huahua:token` → 空响应

### 认证失败影响
- `/rest/api/2/myself` → 空响应（无法识别用户）
- `/rest/api/2/project` → `[]` 空数组（匿名用户无项目可见）
- 任何 JQL 查询 → 返回 "project 域中没有 AIWH 值" / "assignee 不允许匿名用户查看"

---

## 可能原因

1. **Personal Access Token 过期** — Jira Server/Data Center 的 PAT 可能设置了有效期，当前 token 已过期
2. **实例数据重置** — Jira Server 可能经历了数据重置/重建，导致用户、token、项目全部丢失
3. **配置变更** — 认证配置被修改，Bearer Token 方式不再被接受

---

## 无法执行的操作

- ❌ 查询处理中 ticket
- ❌ 查询待领取 ticket  
- ❌ 领取/assign ticket
- ❌ 添加 comment
- ❌ 状态 transition
- ❌ 任何 Jira 写操作

---

## 建议修复步骤

1. **检查 Jira Data Center 用户管理** — 确认 huahua 用户是否仍存在
2. **重新生成 Personal Access Token** — 在 Jira 用户设置中重新生成 PAT
3. **确认认证方式** — Jira Server 9.4.0 可能需要 Basic Auth 而非 Bearer
4. **检查项目数据** — 如果实例被重置，AIWH 项目可能需要重新创建
5. **验证 Jira Cloud 实例状态** — 确认 3pigc.atlassian.net 的订阅/维护状态

---

*下次巡查将继续尝试，但预计会保持 BLOCKED 状态直到认证恢复。*
