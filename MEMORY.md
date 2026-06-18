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

## Promoted From Short-Term Memory (2026-06-19)

<!-- openclaw-memory-promotion:memory:memory/2026-06-14-jira-inspection.md:3:6 -->
- 当前任务状态: 无 active task; 处理中 + huahua 的 ticket: 0; Selected for Development + 未分配的 ticket: 0; AIWH 总 ticket 数: 107 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-14-jira-inspection.md:3-6]
<!-- openclaw-memory-promotion:memory:memory/2026-06-14-jira-inspection.md:7:7 -->
- 所有 ticket 状态: 全部完成 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-14-jira-inspection.md:7-7]
<!-- openclaw-memory-promotion:memory:memory/2026-06-14-jira-inspection.md:9:9 -->
- 结论: 当前没有待处理的 Jira 任务。 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-14-jira-inspection.md:9-9]
<!-- openclaw-memory-promotion:memory:memory/2026-06-14.md:14:17 -->
- Jira API 状态: **BLOCKER: Jira Cloud 不可用**; API 返回: "Page unavailable"; Atlassian Status 页面显示今日无 incident，但实际访问被拒绝; 多次重试均失败（api/2 和 api/3 都返回相同错误） [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-14.md:14-17]
<!-- openclaw-memory-promotion:memory:memory/2026-06-14.md:18:18 -->
- Jira API 状态: Request IDs: 852d6db8071d4e50884ff2d66189afd8, f0a374bc597b4022a615f6c79c470b40, 54ff34baac374711bb52f84c5f2326cc [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-14.md:18-18]
<!-- openclaw-memory-promotion:memory:memory/2026-06-14.md:21:23 -->
- 无法执行的操作: 无法查询"处理中"的 ticket（assignee=huahua）; 无法查询待领取的 ticket（Selected for Development + assignee=EMPTY）; 无法 claim/transition/comment 任何 ticket [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-14.md:21-23]
<!-- openclaw-memory-promotion:memory:memory/2026-06-14.md:31:33 -->
- 修正：使用正确的 Jira DC 地址: 之前错误地使用了 `https://3pigc.atlassian.net` (Jira Cloud); 实际应为 `http://116.205.141.57:50008` (Jira Data Center 9.4.0); wing_recovery_alert.md 历史记录明确指向 DC 地址 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-14.md:31-33]
<!-- openclaw-memory-promotion:memory:memory/2026-06-14.md:6:6 -->
- 当前任务状态: `task_state_manager.py status`: No active task [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-14.md:6-6]
<!-- openclaw-memory-promotion:memory:memory/2026-06-14.md:9:11 -->
- 本地代码状态: 分支: main; 状态: clean，nothing to commit; 与 origin/main 同步 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-14.md:9-11]
<!-- openclaw-memory-promotion:memory:memory/2026-06-14-jira-inspection.md:1:1 -->
- Jira 巡查报告 (2026-06-14 08:47:36) [score=0.802 recalls=0 avg=0.620 source=memory/2026-06-14-jira-inspection.md:1-1]
