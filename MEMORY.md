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

## Promoted From Short-Term Memory (2026-06-17)

<!-- openclaw-memory-promotion:memory:memory/2026-06-11.md:17:20 -->
- 2026-06-11 09:44 Jira 任务巡查: AIWH 项目所有 ticket: **107** 个，全部状态为"完成"; task_state_manager: No active task; Git workspace (~/workspace/wing_1): clean; 结论: **当前没有待处理的 Jira 任务** [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-11.md:17-20]
<!-- openclaw-memory-promotion:memory:memory/2026-06-11.md:26:29 -->
- 2026-06-11 10:04 Jira 任务巡查: 触发器: cron:8d0227c6-23ec-434c-802a-97bdb590dc1f; Jira 地址: http://116.205.141.57:50008; 处理中 (In Progress) + assignee=huahua: **0**; Selected for Development + assignee EMPTY: **0** [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-11.md:26-29]
<!-- openclaw-memory-promotion:memory:memory/2026-06-11.md:30:33 -->
- 2026-06-11 10:04 Jira 任务巡查: AIWH 项目所有 ticket: **107** 个，全部状态为"完成"; task_state_manager: No active task; Git workspace (~/workspace/wing_1): clean; Git status (~/clawd): wing_recovery_alert.md 未提交（09:44 巡查遗留，远程仓库不存在） [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-11.md:30-33]
<!-- openclaw-memory-promotion:memory:memory/2026-06-11.md:4:7 -->
- 2026-06-11 09:30 OpenClaw 自巡检: 状态: ✅ 正常; 主机: mini2 已运行13天，负载正常; Gateway: 健康 (`ok:true`, status=live); Agent: 活跃 [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-11.md:4-7]
<!-- openclaw-memory-promotion:memory:memory/2026-06-11.md:8:9 -->
- 2026-06-11 09:30 OpenClaw 自巡检: 警告: 日志关键词误报，无实际异常; 报告: `/Users/3pigcn/clawd/logs/openclaw_self_inspection/latest.md` [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-11.md:8-9]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12-jira-blocker.md:13:13 -->
- Jira 项目状态摘要: 项目: AIWH [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-12-jira-blocker.md:13-13]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12-jira-blocker.md:16:17 -->
- Jira 项目状态摘要: 已完成: 多个（所有现有 ticket 均为 Done 状态）; 结论: 当前没有待处理的 Jira 任务。 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-12-jira-blocker.md:16-17]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12-jira-blocker.md:20:20 -->
- 说明: 07:24 AM 的 blocker 记录已纠正：Jira 实际地址为 `http://116.205.141.57:50008`，非 `aiwh.atlassian.net`。该站点运行正常。 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-12-jira-blocker.md:20-20]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12-jira-blocker.md:4:4 -->
- 状态: Jira Data Center (http://116.205.141.57:50008) 运行正常，Bearer Token 认证通过。 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-12-jira-blocker.md:4-4]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12-jira-blocker.md:7:10 -->
- 检查步骤: ✅ 检查 "处理中" ticket —— 无处理中的 ticket（状态="处理中" 且 assignee=huahua）; ✅ 检查 "待领取" ticket —— 无待领取的 ticket（状态="Selected for Development" 且 assignee=EMPTY）; ✅ 检查所有未完成 ticket —— 无（所有 AIWH 项目 ticket 状态均为 "Done"）; ✅ 检查本地 git 状态 —— 无未提交代码（仅本文件修改） [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-12-jira-blocker.md:7-10]

## Promoted From Short-Term Memory (2026-06-18)

<!-- openclaw-memory-promotion:memory:memory/2026-06-12-jira-inspection.md:1:4 -->
- Jira任务巡查记录： 时间：2026-06-12 12:15 (Asia/Shanghai) 结果：Jira API 无法访问（HTTP 404，站点显示不可用） Atlassian状态页面：所有系统正常（可能该特定站点有临时问题） [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-12-jira-inspection.md:1-4]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12-jira-inspection.md:7:8 -->
- 没有未提交代码更改; 最近提交：JIRA-CRON巡查记录 [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-12-jira-inspection.md:7-8]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12-jira-inspection.md:9:9 -->
- 行动：BLOCKER - 无法连接Jira，等待服务恢复后重试 [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-12-jira-inspection.md:9-9]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12.md:4:4 -->
- 19:02 - 系统巡检心跳: cron:078443c8-c048-4e69-8dab-eb99c185567b 触发系统巡检脚本。 [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-12.md:4-4]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12.md:6:8 -->
- 19:02 - 系统巡检心跳: K8S日志检查 ✅; 主机资源检查 ✅; HTTP端点检查 ✅ [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-12.md:6-8]
<!-- openclaw-memory-promotion:memory:memory/2026-06-12.md:10:10 -->
- 19:02 - 系统巡检心跳: 无异常，无需 agent 介入。 [score=0.814 recalls=0 avg=0.620 source=memory/2026-06-12.md:10-10]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:10:11 -->
- 04:45 Jira 任务巡查 (cron): [2026-06-13 22:35:41] Jira巡查: Jira Cloud 服务不可用 (Page unavailable) - 状态页面显示无已知问题，但API返回503 [2026-06-13 23:14:20] Jira巡查: 无处理中/无待办任务，AIWH全部完成。Atlassian Cloud仍不可用(6h+)。已提交巡查记录。 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-13.md:10-11]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:4:7 -->
- 04:45 Jira 任务巡查 (cron): **状态**: BLOCKED - Jira 服务不可用; **详情**: Atlassian Cloud 实例 `3pigc.atlassian.net` 返回 "Page unavailable"; **状态页面**: https://status.atlassian.com 显示无已知故障（可能是区域性/临时问题）; **Request ID**: 0f3ba02a4152413b9d8af748a747d4b1 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-13.md:4-7]
<!-- openclaw-memory-promotion:memory:memory/2026-06-13.md:8:9 -->
- 04:45 Jira 任务巡查 (cron): **本地状态**: 无活跃任务，git 工作目录干净; **下一步**: 等待 Jira 恢复后重新巡查 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-13.md:8-9]
