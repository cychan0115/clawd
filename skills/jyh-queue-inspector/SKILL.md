---
name: "jyh-queue-inspector"
description: "Check JYH community Redis queue status on K8S ocr1 cluster"
---

# JYH Queue Inspector

Check how many report generation tasks are queued/pending/done for a specific JYH community.

## Target
- **K8S cluster**: ocr1 (via SSH)
- **Redis**: 10.0.0.6:6379
- **Queue key pattern**: `{prefix}{prefix}_queue_queue_list`
- **Lock key pattern**: `{prefix}user_deal_queue_lock:{prefix}:{queue_id}`

## Usage

### 1. Discover community namespace
```bash
ssh ocr1 "kubectl get namespaces | grep -E '^[a-z]+[0-9]*'"
```

### 2. Get Redis credentials from any pod in the namespace
```bash
ssh ocr1 "kubectl exec -n <namespace> <any-pod> -- env | grep -E 'REDIS_HOST|REDIS_PASSWORD|REDIS_PREFIX'"
```

### 3. Inspect queue (Python via SSH to ocr1 host)
```python
import redis, json
r = redis.Redis(host=REDIS_HOST, port=6379, password=REDIS_PASSWORD, decode_responses=True, protocol=2)
queue_list = r.lrange(f"{REDIS_PREFIX}{REDIS_PREFIX}_queue_queue_list", 0, -1)

# Count by status
completed = 0
pending = 0
processing = 0
for item in queue_list:
    data = json.loads(item)
    content = data.get("content_json", [])
    deal_status = content[3].get("deal_status") if len(content)>=4 and isinstance(content[3], dict) else None
    if deal_status is True: completed += 1
    elif deal_status is False: processing += 1
    else: pending += 1
```

### 4. Report output
```
=== {namespace} 队列统计 ===
队列总数: {total}
  已完成: {completed}
  处理中: {processing}
  待处理: {pending}
活跃队列锁: {lock_count} 个
```

## Queue types observed
- `生成报告（拆）` - batch report generation (20 reports per item)
- `导出Word报告通知` - Word export notification
- `生成报告通知` - single report notification
- `自定义导入答卷` - custom answer import
- `导出Word报告` - Word export

## Safety
- Read-only operation; no queue mutation
- SSH key must be pre-configured for ocr1 access
- Redis password is pulled from pod env, not hardcoded
