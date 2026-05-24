---
title: Jira Ticket Executor
version: 1.0.0
trigger:
  - "execute Jira ticket"
  - "接票"
  - "claim ticket"
  - "处理 AIWH-"
  - "Jira ticket 执行"
context:
  required:
    - Jira ticket key (e.g. AIWH-123)
    - Jira API access
  optional:
    - Git repo access
    - SSH access to target machines
---

# Jira Ticket Executor — huahua/OpenClaw 专用

> 此 SKILL 专门给 **huahua / OpenClaw on mini2** 执行 Jira ticket 时使用。
> Anna/Hermes 负责创建 ticket 和 Review，huahua 负责执行。

## 1. 接票前检查 (Preflight Check)

在 claim ticket 之前，必须确认：

1. **Ticket 状态**是 Backlog 或"待领取"（不是"处理中"或"完成"）
2. **Assignee 为空**（没有被别人领取）
3. **依赖 ticket** 已经标记为 ACCEPTED（不是只是 Done）
4. **描述足够清晰** — 如果有歧义，写 comment 提问，不要自己猜
5. **当前没有正在执行的 ticket**（一次只能 claim 一个）

如果任何检查失败，写 `[BLOCKER]` comment 并停止。

## 2. Claim Ticket (LEASE)

通过 Jira API：
1. 设置 assignee 为自己（huahua / OpenClaw）
2. 状态从 Backlog → 处理中
3. 写 `[LEASE]` comment：

```
[LEASE]
Executor: huahua / OpenClaw on mini2
Timestamp: <ISO8601>
Claiming ticket for execution.
```

## 3. 执行前检查 (Preflight Check)

写 `[Preflight Check]` comment，包含：

```
[Preflight Check]

✅ mini2 online: <hostname>
✅ Repo exists: <repo-path>/.git present
✅ Branch: <branch> @ <commit>
✅ Remote reachable: <remote-status>
✅ Local uncommitted changes: <git-status-output>
✅ Identity overlay risk: <check-result>

Decision: CAN START / BLOCKED
```

如果 CAN START，继续执行。
如果 BLOCKED，写原因并停止。

## 4. 执行任务

按 ticket 描述执行任务：
- 只执行 ticket 范围内的工作
- 不要擅自扩展范围
- 如果发现问题，写 `[BLOCKER]` comment
- 如果执行超过 30 分钟，写 `[Progress Update]` comment

## 5. Done Report

任务完成后写 `[Done Report]` comment：

```
[Done Report]

## Execution Summary
**Executor**: huahua / OpenClaw on mini2
**Timestamp**: <ISO8601>

---

## What Was Done
- <步骤1>
- <步骤2>

## Evidence
- <命令输出或文件路径>
- <git commit hash>

## Verification
✅ <检查项1>
✅ <检查项2>

## Status
✅ COMPLETE
```

## 6. 状态流转

```
Backlog → [LEASE] → 处理中 → [Preflight] → 执行 → [Done Report] → 完成
```

## 7. 关键规则

| 规则 | 说明 |
|------|------|
| 一次一票 | 同时只能 claim 一个 ticket |
| 依赖先验 | 下游 ticket 必须等上游 ACCEPTED 才能开始 |
| 不猜需求 | 描述不清就提问，不自己假设 |
| 30分钟更新 | 超过 30 分钟必须写 Progress Update |
| 有证据 | Done Report 必须包含可验证的证据 |

## 8. 故障处理

| 场景 | 操作 |
|------|------|
| Ticket 描述不清 | 写 comment 提问，等 Anna 回复 |
| 依赖未 ACCEPTED | 写 BLOCKER comment，停止执行 |
| 执行失败 | 写 BLOCKER comment，附错误日志 |
| 需要扩展范围 | 写 comment 请求 Anna 确认 |
| 网络/环境故障 | 写 BLOCKER comment，等恢复 |

## 9. 与 Anna 的协作

- Anna 是 planner / reviewer
- huahua 是 executor
- 所有沟通通过 Jira comment
- 不要私下绕过 Jira 直接执行

## 10. Skill 沉淀

如果某个任务模式重复出现：
1. 执行一次作为 POC
2. 给 Anna 看结果
3. Anna 确认后，沉淀为新的 SKILL.md
4. 更新 Jira ticket 引用新 Skill
