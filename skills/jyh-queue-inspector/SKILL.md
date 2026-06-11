---
name: "jyh-queue-inspector"
description: "Check JYH community DB queue + Redis live status on K8S ocr1"
---

# JYH Queue Inspector

Check report generation task queue for a JYH community.
Uses **MySQL as primary source** (persistent, complete), Redis as optional live supplement.

## Target
- **K8S cluster**: ocr1 (via SSH)
- **DB**: MySQL, pulled from pod env (DB_HOST/DB_PORT/DB_USER/DB_PASSWORD/DB_NAME)
- **Redis**: pulled from pod env (REDIS_HOST/REDIS_PORT/REDIS_PASSWORD/REDIS_PREFIX)

## Primary: DB query (MySQL)

```sql
SELECT status, name, COUNT(*) FROM queue
GROUP BY status, name
ORDER BY status, cnt DESC;
```

| status | meaning |
|--------|---------|
| 0 | pending |
| 1 | processing |
| 2 | done |
| 3 | failed / error |

## Supplemental: Redis (live locks)
- Queue list length for comparison
- Active lock count (how many pods are currently running)

## Usage

Trigger phrases: "check JYH queue", "查队列", "还有多少报告没跑完", "huadu 队列"

### Manual script
```bash
python3 ~/.openclaw/skills/jyh-queue-inspector/scripts/inspect_queue.py huadu
```

## Report output
```
=== {namespace} 队列统计 (DB) ===
总计: 73,601
  待处理: 4,369
  处理中: 30
  已完成: 59,864
  异常/失败: 9,338

待处理分布:
  导出Word报告通知: 2,892
  生成报告（拆）: 796
  生成报告通知: 674

Redis 补充:
  Redis 队列列表: 4,369
  活跃锁: 29 个
```

## Safety
- Read-only DB queries
- SSH key pre-configured for ocr1
- Credentials pulled from pod env, never hardcoded
