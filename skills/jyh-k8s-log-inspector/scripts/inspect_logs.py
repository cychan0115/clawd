#!/usr/bin/env python3
"""JYH K8S Log Inspector — check error logs for a community namespace."""
import sys, subprocess, re

ERROR_PATTERN = 'error|exception|traceback|fatal|panic|crash|failed|timeout|refused|denied|broken|oom|memory.*exhaust|connect.*fail'

def ssh_cmd(cmd):
    return subprocess.run(f"ssh ocr1 '{cmd}'", shell=True, capture_output=True, text=True)

def inspect_logs(ns, since='30m'):
    print(f"=== {ns} K8S 日志检查 ===")
    
    # Pod status
    out = ssh_cmd(f"kubectl get pods -n {ns} --no-headers | wc -l")
    pod_count = int(out.stdout.strip()) if out.returncode == 0 else 0
    
    out = ssh_cmd(f"kubectl get pods -n {ns} --field-selector=status.phase!=Running --no-headers")
    abnormal = out.stdout.strip().split('\n') if out.stdout.strip() else []
    
    print(f"Pod 总数: {pod_count}")
    print(f"  异常 Pod: {len(abnormal)} {'/ ' + str(abnormal)[:200] if abnormal else '(无)'}")
    
    # Restart counts
    out = ssh_cmd(f"kubectl get pods -n {ns} -o jsonpath='{{range .items[*]}}{{.metadata.name}}{{\" \\n\"}}{{.status.containerStatuses[0].restartCount}}{{\"\\n\"}}{{end}}'")
    restarts = [int(x) for x in re.findall(r'\d+', out.stdout) if x.isdigit()]
    total_restarts = sum(restarts)
    print(f"  总重启次数: {total_restarts}")
    
    # Error logs by app type
    selectors = ['', f'app={ns}', f'app={ns}-cron', f'app={ns}-cron-with-print', f'app={ns}-qa']
    total_errors = 0
    for sel in selectors:
        sel_flag = f"--selector={sel}" if sel else "--all-containers"
        cmd = f"kubectl logs -n {ns} {sel_flag} --since={since} 2>/dev/null | grep -iE '{ERROR_PATTERN}' | wc -l"
        out = ssh_cmd(cmd)
        count = int(out.stdout.strip()) if out.returncode == 0 else 0
        total_errors += count
    
    print(f"\n最近 {since} 错误日志:")
    print(f"  匹配关键词: {total_errors} 条")
    
    # Warning events
    out = ssh_cmd(f"kubectl get events -n {ns} --field-selector=type=Warning --sort-by='.lastTimestamp' --no-headers | wc -l")
    warnings = int(out.stdout.strip()) if out.returncode == 0 else 0
    
    out = ssh_cmd(f"kubectl get events -n {ns} --field-selector=type!=Normal --sort-by='.lastTimestamp' --no-headers | wc -l")
    non_normal = int(out.stdout.strip()) if out.returncode == 0 else 0
    
    print(f"K8S 事件:")
    print(f"  Warning 事件: {warnings}")
    print(f"  非 Normal 事件: {non_normal}")
    
    if total_errors == 0 and warnings == 0 and non_normal == 0 and total_restarts == 0 and not abnormal:
        print(f"\n结论: ✅ {ns} 无报错，所有 Pod 健康")
    else:
        print(f"\n结论: ⚠️ {ns} 存在 {total_errors} 条错误日志 / {warnings} 个 Warning 事件，需关注")

if __name__ == '__main__':
    ns = sys.argv[1] if len(sys.argv) > 1 else 'huadu'
    since = sys.argv[2] if len(sys.argv) > 2 else '30m'
    inspect_logs(ns, since)
