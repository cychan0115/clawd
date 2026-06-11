#!/usr/bin/env python3
"""JYH Queue Inspector — check Redis queue status for a community namespace."""
import sys, json, redis, subprocess, re, os

def run_on_ocr1(cmd):
    return subprocess.run(f"ssh ocr1 '{cmd}'", shell=True, capture_output=True, text=True)

def get_namespace_info(ns):
    # Get Redis env from first pod
    out = run_on_ocr1(f"kubectl get pods -n {ns} -o jsonpath='{{.items[0].metadata.name}}'")
    pod = out.stdout.strip()
    out = run_on_ocr1(f"kubectl exec -n {ns} {pod} -- env | grep -E 'REDIS_HOST|REDIS_PASSWORD|REDIS_PORT|REDIS_PREFIX'")
    env = {}
    for line in out.stdout.strip().split('\n'):
        if '=' in line:
            k, v = line.split('=', 1)
            env[k] = v
    return env

def inspect_queue(ns, env):
    host = env.get('REDIS_HOST', '10.0.0.6')
    port = int(env.get('REDIS_PORT', '6379'))
    password = env.get('REDIS_PASSWORD', '')
    prefix = env.get('REDIS_PREFIX', ns)

    r = redis.Redis(host=host, port=port, password=password, decode_responses=True, protocol=2)
    queue_key = f"{prefix}{prefix}_queue_queue_list"
    queue_list = r.lrange(queue_key, 0, -1)

    completed = pending = processing = 0
    completed_reports = pending_reports = processing_reports = 0
    pending_types = {}

    for item in queue_list:
        try:
            data = json.loads(item)
            content = data.get("content_json", [])
            deal_status = None
            if len(content) >= 4 and isinstance(content[3], dict):
                deal_status = content[3].get("deal_status")
            report_count = len(content[0]) if len(content) >= 1 and isinstance(content[0], list) else 0

            if deal_status is True:
                completed += 1; completed_reports += report_count
            elif deal_status is False:
                processing += 1; processing_reports += report_count
            else:
                pending += 1; pending_reports += report_count
                name = data.get("name", "unknown")
                pending_types[name] = pending_types.get(name, 0) + 1
        except Exception:
            pass

    locks = r.keys(f"{prefix}user_deal_queue_lock:{prefix}:*")

    print(f"=== {ns} 队列统计 ===")
    print(f"队列总数: {len(queue_list)}")
    print(f"  已完成: {completed} ({completed_reports} 个报告)")
    print(f"  处理中: {processing} ({processing_reports} 个报告)")
    print(f"  待处理: {pending} ({pending_reports} 个报告)")
    print(f"活跃队列锁: {len(locks)} 个")
    if pending_types:
        print("待处理类型分布:")
        for name, count in sorted(pending_types.items(), key=lambda x: -x[1]):
            print(f"  {name}: {count}")

if __name__ == '__main__':
    ns = sys.argv[1] if len(sys.argv) > 1 else 'huadu'
    env = get_namespace_info(ns)
    inspect_queue(ns, env)
