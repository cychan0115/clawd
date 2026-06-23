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

## Promoted From Short-Term Memory (2026-06-21)

<!-- openclaw-memory-promotion:memory:memory/2026-06-16-jira-inspection.md:12:13 -->
- "待领取" ticket 检查: 状态 = Selected for Development + assignee = EMPTY: **0 tickets**; 状态 = Backlog: **0 tickets** [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-16-jira-inspection.md:12-13]
<!-- openclaw-memory-promotion:memory:memory/2026-06-16-jira-inspection.md:17:19 -->
- 项目整体状态: AIWH 项目总计: **107 tickets**; 所有 ticket 状态: **完成**; 无未完成的 ticket [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-16-jira-inspection.md:17-19]
<!-- openclaw-memory-promotion:memory:memory/2026-06-16-jira-inspection.md:22:22 -->
- 本地任务状态: task_state_manager: No active task ✅ [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-16-jira-inspection.md:22-22]
<!-- openclaw-memory-promotion:memory:memory/2026-06-16-jira-inspection.md:26:26 -->
- 结论: 当前没有待处理的 Jira 任务。所有 ticket 均已完成。 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-16-jira-inspection.md:26-26]
<!-- openclaw-memory-promotion:memory:memory/2026-06-16-jira-inspection.md:5:5 -->
- 巡查结果: **状态: 无待处理任务** ✅ [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-16-jira-inspection.md:5-5]
<!-- openclaw-memory-promotion:memory:memory/2026-06-16-jira-inspection.md:8:9 -->
- "处理中" ticket 检查（优先级最高）: assignee = huahua + 状态 = 处理中: **0 tickets**; 无需检查本地代码状态或执行 commit/push [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-16-jira-inspection.md:8-9]

## Promoted From Short-Term Memory (2026-06-23)

<!-- openclaw-memory-promotion:memory:memory/2026-06-18.md:10:13 -->
- 08:00 早安检查: **天气**: 上海 24°C 多云，体感 26°C，湿度 100%，最高 30°C，UV 9; **菜单**: weekly-meal-plan.md 未填写，无今日菜单; **日历**: 无配置，未检查; **Jira**: 无配置，未检查紧急任务 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-18.md:10-13]
<!-- openclaw-memory-promotion:memory:memory/2026-06-18.md:14:16 -->
- 08:00 早安检查: **系统健康**: ⚠️ 磁盘使用率 95% (/System/Volumes/Data 仅剩 24G)，负载 2.84; **待办**: 建议清理磁盘空间（Caches 7.5G+）; **Action**: 早安消息已发送 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-18.md:14-16]
<!-- openclaw-memory-promotion:memory:memory/2026-06-18.md:4:7 -->
- 06:33 Heartbeat: **Task state**: No active task; **Jira watchdog**: No alerts; **Git status**: Clean; **Action**: Quick check complete, nothing pending. huahua idle. [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-18.md:4-7]

## Promoted From Short-Term Memory (2026-06-24)

<!-- openclaw-memory-promotion:memory:memory/2026-06-19-jira-blocker.md:11:11 -->
- 错误详情: Atlassian 状态页面: 无全局故障报告 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-19-jira-blocker.md:11-11]
<!-- openclaw-memory-promotion:memory:memory/2026-06-19-jira-blocker.md:14:16 -->
- 影响: 无法查询"处理中"的 ticket; 无法查询待领取的 ticket; 无法 claim/transition/comment 任何 ticket [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-19-jira-blocker.md:14-16]
<!-- openclaw-memory-promotion:memory:memory/2026-06-19-jira-blocker.md:19:21 -->
- 后续行动: 等待 Jira Cloud 恢复后重试; 建议 Anna 检查 Jira 实例状态或联系 Atlassian 支持; 本次 cron 巡查跳过，下次心跳/cron 自动重试 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-19-jira-blocker.md:19-21]
<!-- openclaw-memory-promotion:memory:memory/2026-06-19-jira-blocker.md:25:26 -->
- Evidence: Request ID: 12d10b5f86584c5bbd4f781539bde87a Error: {"errorMessage": "Site temporarily unavailable", "errorCode": "OTHER"} [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-19-jira-blocker.md:25-26]
<!-- openclaw-memory-promotion:memory:memory/2026-06-19-jira-blocker.md:4:4 -->
- 状态: Jira Cloud 实例 **不可用**，无法执行 ticket 巡查。 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-19-jira-blocker.md:4-4]
<!-- openclaw-memory-promotion:memory:memory/2026-06-19-jira-blocker.md:7:10 -->
- 错误详情: 端点: `https://aiwriterhub.atlassian.net/rest/api/2/search`; 返回: `{"errorMessage": "Site temporarily unavailable", "errorCode": "OTHER"}` (HTTP 404); 尝试的域名: aiwriterhub.atlassian.net, 3pigc.atlassian.net; 尝试的 API 版本: api/2, api/3 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-19-jira-blocker.md:7-10]
<!-- openclaw-memory-promotion:memory:memory/2026-06-19.md:12:13 -->
- 23:30 - OpenClaw 自巡检: 系统 fallback 机制正常工作; 当前巡检任务本身运行正常，说明服务已恢复 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-19.md:12-13]
<!-- openclaw-memory-promotion:memory:memory/2026-06-19.md:3:5 -->
- 23:30 - OpenClaw 自巡检: **巡检任务**: cron `73bbdaca-9c48-41d7-a333-1c3e2d112c95`; **执行结果**: ✅ 系统整体健康; **报告路径**: `/Users/3pigcn/clawd/logs/openclaw_self_inspection/latest.md` [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-19.md:3-5]
<!-- openclaw-memory-promotion:memory:memory/2026-06-19.md:7:7 -->
- 23:30 - OpenClaw 自巡检: **异常记录**（无需处理，偶发网络波动）： [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-19.md:7-7]
<!-- openclaw-memory-promotion:memory:memory/2026-06-19.md:8:11 -->
- 23:30 - OpenClaw 自巡检: 6月18-19日凌晨 kimi API 不稳定，多个 cron 任务触发 LLM timeout; 涉及 cron: `73bbdaca-9c48-41d7-a333-1c3e2d112c95` 和 `8d0227c6-23ec-434c-802a-97bdb590dc1f`; 错误类型: `fetch failed` / `network connection error` / `LLM request timed out`; 模型降级链: kimi-for-coding → kimi-k2.6 → gpt-5.4 → gpt-4o（最终成功） [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-19.md:8-11]
