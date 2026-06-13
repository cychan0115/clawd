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

## Promoted From Short-Term Memory (2026-06-13)

<!-- openclaw-memory-promotion:memory:memory/2026-06-07-jira-blocker.md:10:11 -->
- 结论: Jira 实例 (3pigc.atlassian.net) 当前不可用，无法执行 ticket 查询和处理。 这是 Atlassian Cloud 服务端问题，非本地网络问题。 [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-07-jira-blocker.md:10-11]
<!-- openclaw-memory-promotion:memory:memory/2026-06-07-jira-blocker.md:14:15 -->
- 本地状态: Git 工作区: clean (no uncommitted changes); Task State: No active task [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-07-jira-blocker.md:14-15]
<!-- openclaw-memory-promotion:memory:memory/2026-06-07-jira-blocker.md:18:18 -->
- 建议: 等待 Atlassian 服务恢复后重试。 [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-07-jira-blocker.md:18-18]
<!-- openclaw-memory-promotion:memory:memory/2026-06-07-jira-blocker.md:4:7 -->
- 检查步骤: 尝试连接 Jira API: https://3pigc.atlassian.net/rest/api/2/search; 返回结果: "Page unavailable" (Atlassian Cloud 服务页面); 检查 Atlassian Status: 状态页面显示无报告事件; 网络连通性: ping 3pigc.atlassian.net 正常 (51ms) [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-07-jira-blocker.md:4-7]
<!-- openclaw-memory-promotion:memory:memory/2026-06-08-jira-blocker.md:10:12 -->
- 影响: 无法查询"处理中"的 ticket（步骤 2）; 无法查询"Selected for Development"的 ticket（步骤 3）; 无法执行任何 Jira API 操作（assign、transition、comment 等） [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-08-jira-blocker.md:10-12]
<!-- openclaw-memory-promotion:memory:memory/2026-06-08-jira-blocker.md:16:16 -->
- 证据: curl -I https://anna-3pigc.atlassian.net/rest/api/2/serverInfo [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-08-jira-blocker.md:16-16]
<!-- openclaw-memory-promotion:memory:memory/2026-06-08-jira-blocker.md:23:25 -->
- 后续行动: 等待 Jira 站点恢复后重试; 下一轮 cron job (21:44) 会自动重试; 如果持续不可用，建议检查 Atlassian 状态页面或联系支持 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-08-jira-blocker.md:23-25]
<!-- openclaw-memory-promotion:memory:memory/2026-06-08-jira-blocker.md:28:28 -->
- 后续行动: 写入时间: 2026-06-08 21:44 (Asia/Shanghai) [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-08-jira-blocker.md:28-28]
<!-- openclaw-memory-promotion:memory:memory/2026-06-08-jira-blocker.md:4:7 -->
- 状态: **Jira 站点**: 不可用（HTTP 404，返回 Page unavailable 维护页面）; **Atlassian 状态页面**: 显示全部正常（All Systems Operational），但实际情况不符; **本地代码状态**: 干净，无未提交变更（上次提交 f000353）; **Task State Manager**: 无活跃任务 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-08-jira-blocker.md:4-7]
<!-- openclaw-memory-promotion:memory:memory/2026-06-08-jira-inspection.md:12:12 -->
- 检查项: ✅ 本地 git 状态 → 工作树干净，3 个未推送 commits + 1 个新提交（本地记录） [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-08-jira-inspection.md:12-12]

## Promoted From Short-Term Memory (2026-06-14)

<!-- openclaw-memory-promotion:memory:memory/2026-06-08-jira-inspection.md:17:20 -->
- Jira Cloud: 从 14:14 CST 开始返回 404; 当前 15:17 CST，仍然不可用; 无法查询任何 ticket 状态; 无法领取或完成任务 [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-08-jira-inspection.md:17-20]
<!-- openclaw-memory-promotion:memory:memory/2026-06-08-jira-inspection.md:23:26 -->
- GitHub / Git 仓库: GitHub API 确认仓库 `cychan0115/clawd` 不存在; GitHub 网页服务 504 超时; 本地有 3 个未推送 commits（14:24-14:34 的巡查记录）; 本次巡查新增 1 个本地提交（记录当前状态） [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-08-jira-inspection.md:23-26]
<!-- openclaw-memory-promotion:memory:memory/2026-06-08-jira-inspection.md:29:32 -->
- 结论: **无待处理的 Jira 任务**（task_state_manager 确认）; **Jira Cloud 服务不可用**，无法进行正常的任务领取/处理流程; **GitHub 远程仓库不存在**，本地 commits 无法同步; 这是一个系统级阻塞，需要等待外部服务恢复 [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-08-jira-inspection.md:29-32]
<!-- openclaw-memory-promotion:memory:memory/2026-06-08-jira-inspection.md:5:5 -->
- 状态: ⚠️ **多项服务不可用** — 无法执行 Jira 任务处理 [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-08-jira-inspection.md:5-5]
<!-- openclaw-memory-promotion:memory:memory/2026-06-08-jira-inspection.md:8:11 -->
- 检查项: ❌ Jira Cloud 主站 → 404（维护中，已持续约63分钟）; ❌ GitHub 仓库 → 不存在（API 404）; ❌ GitHub 服务 → 504 Gateway Timeout; ✅ 本地任务状态 → No active task [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-08-jira-inspection.md:8-11]
<!-- openclaw-memory-promotion:memory:memory/2026-06-08.md:1:1 -->
- 2026-06-08 14:16 CST Jira cron巡查: Jira Cloud 维护中，无活跃任务，git干净。 [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-08.md:1-1]
<!-- openclaw-memory-promotion:memory:memory/2026-06-09.md:12:15 -->
- 检查证据: 处理中查询: `total: 0`（Jira Data Center API HTTP 200）; 待领取查询: `total: 0`（Jira Data Center API HTTP 200）; task_state_manager: `No active task`; Git 工作树: 干净（无未提交代码） [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-09.md:12-15]
<!-- openclaw-memory-promotion:memory:memory/2026-06-09.md:16:16 -->
- 检查证据: 远程仓库: 404（不影响本次结论） [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-09.md:16-16]
<!-- openclaw-memory-promotion:memory:memory/2026-06-09.md:19:19 -->
- 结论: 当前没有待处理的 Jira 任务。 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-09.md:19-19]
<!-- openclaw-memory-promotion:memory:memory/2026-06-09.md:6:9 -->
- 检查项目: 处理中 (In Progress) + assignee=huahua: **0 个**; 待领取 (Selected for Development) + assignee EMPTY: **0 个**; 整个 AIWH 项目"处理中": **0 个**; 整个项目"待领取": **0 个** [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-09.md:6-9]
