---
name: "jyh-queue-inspector"
description: "Fast JYH community queue count check on K8S ocr1"
---

# JYH Queue Inspector

Quickly check queue counts for a JYH community. Fast by default, detail optional.

## Target
- **K8S cluster**: ocr1 (via SSH)
- **DB**: MySQL, pulled from pod env

## Fast query (default)
```sql
SELECT status, COUNT(*) FROM queue GROUP BY status;
```

| status | meaning |
|--------|---------|
| 0 | pending |
| 1 | processing |
| 2 | done |
| 3 | failed |

## Detail query (--detail flag)
```sql
SELECT status, name, COUNT(*) FROM queue GROUP BY status, name;
```

## Usage
Trigger: "查 huadu 队列" / "huadu 多少报告" / "队列状态"

```bash
# Fast (default)
python3 scripts/inspect_queue.py huadu

# With detail
python3 scripts/inspect_queue.py huadu --detail
```

## Report output
```
=== huadu 队列 ===
待处理: 11
处理中: 0
已完成: 64372
异常: 9338
总计: 73721
```

## Safety
- Read-only
- SSH key pre-configured for ocr1
- Credentials from pod env, cached locally after first run
