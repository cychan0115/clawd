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

## Promoted From Short-Term Memory (2026-06-10)

<!-- openclaw-memory-promotion:memory:memory/2026-06-03-jira-patrol.md:25:28 -->
- 本地状态: 最新 commit: `65f2226` - JIRA-PATROL: 20260603_1205 - 无待处理任务，更新巡查记忆; Branch: main; 工作区: clean (after commit); Recovery alert: 无 [score=0.830 recalls=0 avg=0.620 source=memory/2026-06-03-jira-patrol.md:25-28]
<!-- openclaw-memory-promotion:memory:memory/2026-06-03-jira-patrol.md:8:11 -->
- 检查项: [x] 本地任务状态检查 - **无活跃任务** (task_state_manager.py status); [x] Git 工作区检查 - **有未提交文件** (memory/2026-06-03-jira-patrol.md)，已 commit; [x] Git push 状态 - **失败** (SSH auth issue to github.com:3pigcn/clawd.git); [x] Jira API 连接检查 - **正常** (http://116.205.141.57:50008) [score=0.830 recalls=0 avg=0.620 source=memory/2026-06-03-jira-patrol.md:8-11]
<!-- openclaw-memory-promotion:memory:memory/2026-06-03.md:11:14 -->
- 23:14 巡查: **Jira 服务**: 正常; **处理中 ticket**: 0; **待领取 ticket**: 0; **结论**: 无待处理任务 [score=0.830 recalls=0 avg=0.620 source=memory/2026-06-03.md:11-14]
<!-- openclaw-memory-promotion:memory:memory/2026-06-03.md:23:23 -->
- 23:44 巡查: 所有 AIWH 项目 ticket (107个) 均处于完成状态。 [score=0.830 recalls=0 avg=0.620 source=memory/2026-06-03.md:23-23]
<!-- openclaw-memory-promotion:memory:memory/2026-06-03.md:4:7 -->
- 23:54 巡查: **Jira 服务**: 正常 (http://116.205.141.57:50008); **处理中 ticket**: 0; **待领取 ticket**: 0; **本地代码状态**: 干净 (无未提交/未推送) [score=0.830 recalls=0 avg=0.620 source=memory/2026-06-03.md:4-7]
<!-- openclaw-memory-promotion:memory:memory/2026-06-03.md:8:8 -->
- 23:54 巡查: **结论**: 当前没有待处理的 Jira 任务 [score=0.830 recalls=0 avg=0.620 source=memory/2026-06-03.md:8-8]
<!-- openclaw-memory-promotion:memory:memory/2026-06-04.md:14:17 -->
- 结论: **当前没有待处理的 Jira 任务**; Jira 服务已恢复正常（之前巡查记录显示曾不可用）; 本地无遗留代码需要提交; 无需执行任何操作 [score=0.830 recalls=0 avg=0.620 source=memory/2026-06-04.md:14-17]
<!-- openclaw-memory-promotion:memory:memory/2026-06-04.md:20:20 -->
- 结论: *自动巡查记录 - cron: 8d0227c6-23ec-434c-802a-97bdb590dc1f* [score=0.830 recalls=0 avg=0.620 source=memory/2026-06-04.md:20-20]
<!-- openclaw-memory-promotion:memory:memory/2026-06-04.md:4:7 -->
- 检查项: | 检查项 | 结果 | |--------|------| | Jira API 可达性 | ✅ 正常 (116.205.141.57:50008) | | 处理中 (In Progress) + assignee=huahua | ✅ 无 (0) | [score=0.830 recalls=0 avg=0.620 source=memory/2026-06-04.md:4-7]
<!-- openclaw-memory-promotion:memory:memory/2026-06-04.md:8:11 -->
- 检查项: | 待领取 (Selected for Development) + assignee=EMPTY | ✅ 无 (0) | | 所有未分配非完成 ticket | ✅ 无 (0) | | 本地 Git 工作树 | ✅ clean | | 活跃任务状态 | ✅ 无 (No active task) | [score=0.830 recalls=0 avg=0.620 source=memory/2026-06-04.md:8-11]

## Promoted From Short-Term Memory (2026-06-11)

<!-- openclaw-memory-promotion:memory:memory/2026-06-05.md:12:14 -->
- ⚠️ 异常项: **gateway 日志异常**; `web_fetch failed: 400` (1 次) + `404` (2 次) — 外部网站访问失败; `exec failed: sandbox requires a sandbox runtime` (3 次) — 6/4 的 exec 工具配置问题 [score=0.851 recalls=0 avg=0.620 source=memory/2026-06-05.md:12-14]
<!-- openclaw-memory-promotion:memory:memory/2026-06-05.md:17:20 -->
- 系统状态: 负载: 2.44-2.56 (正常); 内存: 85% 空闲，无 swap; 运行时长: 6 天 20 小时; Gateway: 健康，端口 18789 正常 [score=0.851 recalls=0 avg=0.620 source=memory/2026-06-05.md:17-20]
<!-- openclaw-memory-promotion:memory:memory/2026-06-05.md:25:27 -->
- 下一步: Data 卷 95% 需关注，待评估是否需要清理; exec sandbox 错误需检查是否有未配置 sandbox 的 agent 在使用 exec; web_fetch 400/404 可能是外部网站临时问题，持续观察 [score=0.851 recalls=0 avg=0.620 source=memory/2026-06-05.md:25-27]
<!-- openclaw-memory-promotion:memory:memory/2026-06-05.md:5:5 -->
- 04:30 OpenClaw 自巡检 (cron): [巡检报告](../logs/openclaw_self_inspection/latest.md) [score=0.851 recalls=0 avg=0.620 source=memory/2026-06-05.md:5-5]
<!-- openclaw-memory-promotion:memory:memory/2026-06-05.md:8:11 -->
- ⚠️ 异常项: **Data 卷使用率 95%** (`/System/Volumes/Data`); 主磁盘 / 使用率 41%（正常）; Data 卷 400Gi/460Gi 已用，仅 26Gi 可用; 建议：清理大文件或检查是否有日志膨胀 [score=0.851 recalls=0 avg=0.620 source=memory/2026-06-05.md:8-11]
<!-- openclaw-memory-promotion:memory:memory/2026-06-05.md:21:22 -->
- 系统状态: Agent: 活跃; Cron: 正常 [score=0.841 recalls=0 avg=0.620 source=memory/2026-06-05.md:21-22]
<!-- openclaw-memory-promotion:memory:memory/2026-06-03.md:17:20 -->
- 23:44 巡查: **Jira 服务**: 正常; **处理中 ticket**: 0; **待领取 ticket**: 0; **结论**: 无待处理任务 [score=0.834 recalls=0 avg=0.620 source=memory/2026-06-03.md:17-20]
<!-- openclaw-memory-promotion:memory:memory/2026-06-06-jira-blocked.md:11:14 -->
- 已尝试的 API 端点:: `GET /rest/api/2/search?jql=project=AIWH...` → 404 Page Unavailable; `GET /rest/api/3/search?jql=project=AIWH...` → 404 Page Unavailable; `GET /rest/api/3/myself` → 404; `GET /rest/api/2/project/AIWH` → 404 Page Unavailable [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-06-jira-blocked.md:11-14]
<!-- openclaw-memory-promotion:memory:memory/2026-06-06-jira-blocked.md:17:18 -->
- Atlassian 状态页面:: https://status.atlassian.com 显示 "No incidents reported today"; 但实际服务不可用，可能是未报告的区域性问题 [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-06-jira-blocked.md:17-18]
<!-- openclaw-memory-promotion:memory:memory/2026-06-06-jira-blocked.md:21:23 -->
- 本地状态:: Git 工作目录: clean (nothing to commit, working tree clean); 分支: main; task_state_manager: No active task. [score=0.812 recalls=0 avg=0.620 source=memory/2026-06-06-jira-blocked.md:21-23]
