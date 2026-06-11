---
name: "jyh-k8s-log-inspector"
description: "Check JYH community K8S pod error logs on ocr1 cluster"
---

# JYH K8S Log Inspector

Check error/crash/fatal logs for all pods of a JYH community namespace on the ocr1 K8S cluster.

## Target
- **K8S cluster**: ocr1 (via SSH)
- **Namespace pattern**: one namespace per community (e.g. `huadu`, `jyh`, `jyh003`, `jyh011`)
- **Pod labels**: `app=<namespace>`, `app=<namespace>-cron`, `app=<namespace>-qa`, `app=<namespace>-cron-with-print`

## Usage

### 1. List community namespaces
```bash
ssh ocr1 "kubectl get namespaces | grep -E '^[a-z]+[0-9]*'"
```

### 2. Check pod status
```bash
ssh ocr1 "kubectl get pods -n <namespace> --show-labels"
```

### 3. Check error logs (last N minutes)
```bash
# All pods, all containers
ssh ocr1 "kubectl logs -n <namespace> --all-containers --since=30m | grep -iE 'error|exception|traceback|fatal|panic|crash|failed|timeout|refused|denied|broken|oom|memory.*exhaust|connect.*fail' | head -30"

# By selector
ssh ocr1 "kubectl logs -n <namespace> --selector=app=<namespace> --since=30m | grep -iE 'error|exception|traceback|fatal|panic|crash' | head -20"
ssh ocr1 "kubectl logs -n <namespace> --selector=app=<namespace>-cron --since=30m | grep -iE 'error|exception|traceback|fatal|panic|crash' | head -20"
ssh ocr1 "kubectl logs -n <namespace> --selector=app=<namespace>-qa --since=30m | grep -iE 'error|exception|traceback|fatal|panic|crash' | head -20"
```

### 4. Check K8S events
```bash
# Warning events
ssh ocr1 "kubectl get events -n <namespace> --field-selector=type=Warning --sort-by='.lastTimestamp' | head -20"

# All non-Normal events
ssh ocr1 "kubectl get events -n <namespace> --field-selector=type!=Normal --sort-by='.lastTimestamp' | head -20"
```

### 5. Check restart counts
```bash
ssh ocr1 "kubectl get pods -n <namespace> -o jsonpath='{range .items[*]}{.metadata.name}{\" \"}{.status.containerStatuses[0].restartCount}{\"\\n\"}{end}'"
```

## Report output
```
=== <namespace> K8S 日志检查 ===
Pod 状态: 全部 Running / X 个异常
重启次数: 0 (正常) / N (异常)
错误日志:
  ERROR / Exception / Traceback: 0
  Fatal / Panic / Crash: 0
  Timeout / Refused / Connection: 0
K8S 事件:
  Warning 事件: 0
  非 Normal 事件: 0
结论: 无报错 / 发现 X 条错误需关注
```

## Safety
- Read-only; no pod mutation
- SSH key must be pre-configured for ocr1
- Previous container logs only if pod has restarted
