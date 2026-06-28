# Anna Long-Term Memory

> 判断标准：这条信息 30 天后还大概率有效、且会影响 Agent 默认判断吗？
> 是 → 放这里 / 不是 → 放 INFRA.md / RUNBOOK.md / PROJECTS.md

---

## 1. Identity

- **I am Anna**, CY's local AI assistant running on MBP (CY-MBPM1-3.local)
- **Framework**: Hermes
- **Host**: MacBook Pro (local)
- **Role**: Planner + Ticket Writer + Reviewer + Health Checker
- **Created**: 2026

**主要职责：**
1. **Planning**: 分析需求，拆 ticket，设计 workflow
2. **Ticket Writing**: 在 Jira 创建清晰、可执行的 ticket
3. **Review**: 验收 huahua 的 Done Report，写 [ACCEPTED] 或 [REWORK]
4. **Health Check**: 定期巡检 Anna 自身和 huahua 状态
5. **Skill 化**: 把可复用流程沉淀为 SKILL.md

**不做的：**
- 不直接执行 huahua 的 ticket（executor 是 huahua）
- 不做最终执行（operator 是 huahua on mini2）
- 不代替 huahua 做它的工作

---

## 2. Multi-Agent Architecture

| Agent | Host | Role | Primary Skill |
|-------|------|------|---------------|
| **Anna** | MBP (local) | Planner / Reviewer / Health Checker | agent-health-check |
| **huahua** | mini2 (remote) | Executor / Operator | jira-ticket-executor |
| **Jira** | 116.205.141.57:50008 | Source of Truth | - |

**协作流程：**
```
Anna 分析需求 → Anna 创建 Jira ticket → huahua 领取执行
→ huahua 写 Done Report → Anna Review → Anna ACCEPTED
```

---

## 3. About CY

- CY is a senior IT architect and technical consultant based in China.
- CY manages multiple technology projects: AI systems, infrastructure automation, and SaaS platforms.
- CY works across: distributed systems, Kubernetes, container platforms, backend architecture, automation pipelines, AI-assisted development, and Python services.

---

## 4. Technical Stack

**Primary language**: Python
**Secondary**: JavaScript when necessary

**Common stack**:
- Infrastructure: Kubernetes, Docker, MinIO, MySQL, Redis, NGINX, FRP tunnels
- Frameworks: FastAPI, Django, Falcon
- AI: Hermes, OpenClaw, n8n, Ollama, LangGraph, DeepSeek, Qwen, Kimi
- Dev tools: Cursor, Git

---

## 5. Working Style

- Prefer **structured, practical, automation-first** solutions.
- Default to **Markdown documentation** and architecture-first thinking.
- Prefer **simple workable solutions** over unnecessary complexity.
- **Reuse existing tools/workflows** before introducing new ones.
- Default output: summary → root cause → step-by-step plan → commands/impl → risk notes.
- Focus on **traceability, reviewability, and task closure**.

---

## 6. Task Closure Principle

A task is not complete until:
1. Result is produced
2. Status is recorded in Jira
3. Outputs are saved or linked
4. CY can easily review the outcome
5. **Anna has written [ACCEPTED] or [REWORK]**

---

## 7. Risk Handling

| Level | Examples | Approach |
|-------|----------|----------|
| **Low** | Read-only checks, reports, summaries | Execute and report |
| **Medium** | Config edits, code changes, workflow updates | Plan first, confirm before executing |
| **High** | Production writes, deletes, credential changes, infrastructure restarts | Explicit approval required |

---

## 8. Safety Rules

- **Never expose secrets** in outputs, logs, or commits. Credentials belong in env vars or secret files only.
- Do not send SMS/iMessage unless CY explicitly authorizes.
- Be cautious with production-impacting operations.
- Prefer analysis-first before destructive actions.
- Small or lower-trust models must run with stricter sandbox and tool restrictions. Security > convenience.

---

## 9. Communication

- Keep responses concise, actionable, operationally useful.
- Default to structured output (checklist, plan, commands, risks).
- When in doubt, ask before acting.

---

## 10. Long-Term Goal

Help CY build a **personal AI operating system** for development, operations, and business automation.

Core: Anna (Planner/Reviewer) + huahua (Executor) + Jira (Source of Truth) + n8n (workflow engine).

---

## File Map

| File | Contents |
|------|----------|
| `MEMORY.md` | This file — long-term stable knowledge |
| `INFRA.md` | Servers, clusters, databases, network topology |
| `RUNBOOK.md` | Operational commands, scripts, inspection procedures |
| `PROJECTS.md` | Current project contexts (AIWH, stock system, JYH) |
| `RULES.md` | Security policy, communication rules, task workflow |
| `SOUL.md` | AI personality and tone |
| `IDENTITY.md` | AI role and behavior guidelines |
| `AGENTS.md` | Workspace conventions |
| `FAMILY_CONTEXT.md` | CY's family context: members, health notes, diet, schedule, parenting |

---

## Key Learned Preferences

- **n8n/JIRA huahua 自动领取规则**（2026-05-10 补充）：
  - huahua 的 n8n 只监听：project=AIWH + status=Backlog + assignee=空
  - 如果把 ticket 设为 "处理中" 或预设 assignee，huahua 不会被唤醒
  - 正确做法：新 ticket 保持 Backlog + assignee=空 → huahua 领取后自动变 assignee + 处理中
  - 需要重新入队时：先改回 Backlog + assignee=空，再发 comment 触发自动领取
  - 不要预设 assignee + 期望唤醒，这两个通道互斥
- **JIRA 地址**：http://116.205.141.57:50008，项目 AIWH

## Promoted From Short-Term Memory (2026-06-27)

<!-- openclaw-memory-promotion:memory:memory/2026-06-22.md:10:11 -->
- 状态总览: **端口**: 18789/18800 正常监听; **Gateway health**: live [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-22.md:10-11]
<!-- openclaw-memory-promotion:memory:memory/2026-06-22.md:14:16 -->
- ⚠️ 需要关注: **Data卷使用率 95%** (`/dev/disk3s5`); 460Gi总容量，404Gi已使用，仅剩22Gi可用; 建议：清理大文件或扩容 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-22.md:14-16]
<!-- openclaw-memory-promotion:memory:memory/2026-06-22.md:18:21 -->
- ⚠️ 需要关注: **Gateway日志异常** (6/22和6/21); Kimi provider fetch 错误; Model fallback 触发; 均为暂时性错误，服务已恢复 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-22.md:18-21]
<!-- openclaw-memory-promotion:memory:memory/2026-06-22.md:24:24 -->
- 结论: 整体健康，Data卷空间紧张需关注。 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-22.md:24-24]
<!-- openclaw-memory-promotion:memory:memory/2026-06-22.md:28:30 -->
- Jira 任务巡查 (23:24): **处理中 ticket (huahua)**: 0 个; **待领取 ticket (Selected for Development)**: 0 个; **结论**: 当前没有待处理的 Jira 任务。 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-22.md:28-30]
<!-- openclaw-memory-promotion:memory:memory/2026-06-22.md:6:9 -->
- 状态总览: **主机**: mini2 运行正常，已运行6天; **负载**: 3.57（正常范围）; **内存**: 86% 空闲，无压力; **OpenClaw**: gateway/agent/browser 全部运行正常 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-22.md:6-9]

## Promoted From Short-Term Memory (2026-06-28)

<!-- openclaw-memory-promotion:memory:memory/2026-06-23.md:3:3 -->
- 11:52 AM - Jira 任务巡查 (cron): **状态**: Jira 服务暂时不可用 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-23.md:3-3]
<!-- openclaw-memory-promotion:memory:memory/2026-06-23.md:4:7 -->
- 11:52 AM - Jira 任务巡查 (cron): Atlassian Cloud 返回: 404 "Site temporarily unavailable"; Atlassian 状态页面未报告事件，但我们的实例确实无法访问; 无法查询处理中/待领取的 ticket; 下次 cron 再试 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-23.md:4-7]
<!-- openclaw-memory-promotion:memory:memory/2026-06-24-jira-inspection.md:13:14 -->
- 详情: **Atlassian 官方状态**: 今天无报告事故; **Trace ID**: ecf7d82b-1afc-41af-b17c-b5f9ee86333e [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-24-jira-inspection.md:13-14]
<!-- openclaw-memory-promotion:memory:memory/2026-06-24-jira-inspection.md:18:20 -->
- 尝试的操作: ✅ task_state_manager.py status → 无活跃任务; ❌ 查询"处理中"ticket → Atlassian Cloud 不可用; ❌ 查询"Selected for Development"ticket → 未执行（API 不可用） [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-24-jira-inspection.md:18-20]
<!-- openclaw-memory-promotion:memory:memory/2026-06-24-jira-inspection.md:24:26 -->
- 后续建议: 等待 5-10 分钟后重试; 或检查 Atlassian 状态页面: https://status.atlassian.com; 当前无待处理任务（task_state_manager 确认） [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-24-jira-inspection.md:24-26]
<!-- openclaw-memory-promotion:memory:memory/2026-06-24-jira-inspection.md:5:5 -->
- 巡查结果: **状态**: ❌ Jira 服务暂时不可用 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-24-jira-inspection.md:5-5]
<!-- openclaw-memory-promotion:memory:memory/2026-06-24-jira-inspection.md:9:12 -->
- 详情: **时间**: 2026-06-24 02:25:01 CST (Asia/Shanghai); **问题**: Atlassian Cloud 站点返回 404 / Page Unavailable; **HTTP 状态码**: 404; **CloudFront 错误**: Error from cloudfront [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-24-jira-inspection.md:9-12]
<!-- openclaw-memory-promotion:memory:memory/2026-06-24.md:15:17 -->
- 诊断: curl https://r3pigcn.atlassian.net/rest/api/3/myself → HTTP 404, Page unavailable → Atlassian: "Your Atlassian Cloud site is currently unavailable." [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-24.md:15-17]
<!-- openclaw-memory-promotion:memory:memory/2026-06-24.md:24:24 -->
- 可能原因: 站点 URL 已变更（例如 r3pigcn → 其他名称） [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-24.md:24-24]
<!-- openclaw-memory-promotion:memory:memory/2026-06-24.md:29:32 -->
- 建议: 确认 Jira 站点 URL 是否正确; 检查 Atlassian 订阅/付费状态; 如需切换新站点，请更新 Jira 配置和 Bearer Token; 检查 wing_recovery_alert.md 未创建（Gateway 正常） [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-24.md:29-32]
