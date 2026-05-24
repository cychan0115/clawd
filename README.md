# Anna (Hermes) vs huahua (OpenClaw) 多 Agent 协同文档

## 架构

| Agent | Host | Framework | Role | Primary Skill |
|-------|------|-----------|------|---------------|
| **Anna** | MBP (local) | Hermes | Planner / Reviewer / Health Checker | `skills/agent-health-check/SKILL.md` |
| **huahua** | mini2 (remote) | OpenClaw | Executor / Operator | `skills-huahua/jira-ticket-executor/SKILL.md` |
| **Jira** | 116.205.141.57:50008 | - | Source of Truth | - |

## 协作流程

```
Anna 分析需求 → Anna 创建 Jira ticket (Backlog + assignee=空)
→ huahua auto-claim → huahua 执行 → huahua 写 Done Report
→ Anna Review → Anna [ACCEPTED] / [REWORK]
```

## 目录结构

### Anna (本地 MBP)
- `AGENTS.md` — 工作空间入口规则
- `SOUL.md` — Anna 人设 (Planner/Reviewer)
- `MEMORY.md` — Anna 长期记忆
- `MULTI_AGENT_ENTRYPOINT.md` — 多 Agent 协同入口（含 Jira Credentials）
- `MULTI_AGENT_JIRA_WORKFLOW.md` — Jira 协同工作流详细规则
- `AGENT_OBSERVABILITY.md` — Agent 可观察性规则
- `RULES.md` — 行为、安全、工作流规则
- `skills/agent-health-check/SKILL.md` — **Anna 专用：Agent 健康检查**
- `skills/jira-ticket-executor-reference/` — **参考文档（不触发）**：huahua 执行流程参考

### huahua (远程 mini2)
- `AGENTS.md` — 工作空间入口规则
- `SOUL.md` — huahua 人设 (Executor)
- `MEMORY.md` — huahua 长期记忆
- `MULTI_AGENT_ENTRYPOINT.md` — 多 Agent 协同入口
- `MULTI_AGENT_JIRA_WORKFLOW.md` — Jira 协同工作流
- `AGENT_OBSERVABILITY.md` — Agent 可观察性规则
- `RULES.md` — 行为、安全、工作流规则
- `skills-huahua/jira-ticket-executor/SKILL.md` — **huahua 专用：执行 Jira ticket**
- `skills/agent-health-check/SKILL.md` — **huahua 专用：仅报告自身状态**

## 关键规则

1. **Anna 不执行 ticket**：Anna 是 Planner/Reviewer，不执行 huahua 的 ticket
2. **huahua 不做验收**：huahua 是 Executor，必须等 Anna 写 [ACCEPTED]
3. **huahua 不做全局 Health Check**：全局 Health Check 由 Anna 做，huahua 只报告自身状态
4. **所有沟通通过 Jira**：不私下绕过 Jira

## 当前配置

- Anna Jira: openclaw-admin (token_name=hermes)
- huahua 主模型: kimi/kimi-for-coding
- huahua fallbacks: kimi/kimi-k2.6, minimax-portal/MiniMax-M2.7-highspeed
