---
name: "jyh-queue-clearer"
description: "Cancel JYH community pending queue tasks by marking them done in DB"
---

# JYH Queue Clearer

Cancel pending/processing report generation tasks for a JYH community by updating their DB status to "done".

## Target
- **K8S cluster**: ocr1 (via SSH)
- **DB**: MySQL, pulled from pod env (DB_HOST/DB_PORT/DB_USER/DB_PASSWORD/DB_NAME)

## What it does
- Updates `queue` table rows where `status IN (0, 1)` to `status = 2`
- Does **NOT** delete any records — preserves history
- Does **NOT** affect already-completed (`status=2`) or failed (`status=3`) tasks

## Safety rules
- **Always preview first** — show count of affected rows before updating
- **Require explicit confirmation** — user must say "confirm" or "执行" after seeing preview
- Never run against production without user approval

## Workflow

### 1. Get DB credentials from pod env
```bash
ssh ocr1 "kubectl get pods -n <namespace> -o jsonpath='{.items[0].metadata.name}'"
ssh ocr1 "kubectl exec -n <namespace> <pod> -- env | grep -E 'DB_HOST|DB_PORT|DB_USER|DB_PASSWORD|DB_NAME'"
```

### 2. Preview affected rows
```sql
SELECT status, name, COUNT(*) as cnt
FROM queue WHERE status IN (0, 1)
GROUP BY status, name;
```

### 3. Execute update (after user confirmation)
```sql
UPDATE queue
SET status = 2,
    update_time = NOW(6),
    error_log = COALESCE(error_log, '') + ' [BATCH_CANCELLED by agent @ ' + NOW() + ']'
WHERE status IN (0, 1);
```

### 4. Verify result
```sql
SELECT status, COUNT(*) FROM queue GROUP BY status;
```

## Trigger phrases
- "取消 huadu 队列"
- "把 huadu 待处理改成完成"
- "清空 jyh 队列"
- "停止所有报告生成任务"

## Manual script
```bash
python3 ~/.openclaw/skills/jyh-queue-clearer/scripts/clear_queue.py huadu --preview
python3 ~/.openclaw/skills/jyh-queue-clearer/scripts/clear_queue.py huadu --execute
```

## Report output
```
=== huadu 队列取消 ===
预览:
  待处理 (status=0): 4,369
  处理中 (status=1): 30
  总计受影响: 4,399

已执行 UPDATE，4,399 行已标记为完成 (status=2)

验证:
  待处理: 0
  处理中: 0
  已完成: 64,263 (+4,399)
  异常: 9,338
```
