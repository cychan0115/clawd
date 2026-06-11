#!/usr/bin/env python3
"""JYH Queue Inspector — check DB queue + Redis live status for a community namespace."""
import sys, subprocess, re

def run_on_ocr1(cmd, timeout=15):
    r = subprocess.run(f"ssh ocr1 '{cmd}'", shell=True, capture_output=True, text=True, timeout=timeout)
    return r.stdout.strip(), r.stderr.strip(), r.returncode

def get_pod_env(ns, pattern='DB_HOST|DB_PASSWORD|DB_NAME|DB_USER|DB_PORT|REDIS_HOST|REDIS_PASSWORD|REDIS_PORT|REDIS_PREFIX'):
    out, err, rc = run_on_ocr1(f"kubectl get pods -n {ns} -o jsonpath='{{.items[0].metadata.name}}'")
    if rc != 0:
        print(f"Failed to get pod: {err}")
        return {}
    pod = out.strip()
    out, err, rc = run_on_ocr1(f"kubectl exec -n {ns} {pod} -- env | grep -E '{pattern}'")
    env = {}
    for line in out.strip().split('\n'):
        if '=' in line:
            k, v = line.split('=', 1)
            env[k] = v
    return env

def db_query(ns, env):
    host = env.get('DB_HOST', '')
    port = env.get('DB_PORT', '3306')
    user = env.get('DB_USER', 'root')
    password = env.get('DB_PASSWORD', '')
    dbname = env.get('DB_NAME', '')
    if not all([host, password, dbname]):
        print(f"Incomplete DB env for {ns}")
        return None
    
    sql = """
SELECT status, name, COUNT(*) as cnt,
    MIN(create_time) as earliest, MAX(create_time) as latest
FROM queue
GROUP BY status, name
ORDER BY status, cnt DESC;
"""
    cmd = f"mysql -h {host} -P {port} -u {user} -p'{password}' -D {dbname} -e \"{sql}\""
    out, err, rc = run_on_ocr1(cmd, timeout=30)
    if rc != 0:
        print(f"DB query failed: {err[:200]}")
        return None
    return out

def redis_summary(ns, env):
    host = env.get('REDIS_HOST', '')
    port = env.get('REDIS_PORT', '6379')
    password = env.get('REDIS_PASSWORD', '')
    prefix = env.get('REDIS_PREFIX', ns)
    if not all([host, password]):
        return None
    
    script = f"""import redis
r = redis.Redis(host='{host}', port={port}, password='{password}', decode_responses=True, protocol=2)
prefix = '{prefix}'
queue_key = f"{{prefix}}{{prefix}}_queue_queue_list"
qlen = r.llen(queue_key)
locks = r.keys(f"{{prefix}}user_deal_queue_lock:{{prefix}}:*")
print(f"Redis队列列表: {{qlen}}")
print(f"活跃锁: {{len(locks)}}")
"""
    out, err, rc = run_on_ocr1(f"python3 -c '{script}'", timeout=15)
    if rc != 0:
        return None
    return out

def parse_db_output(raw):
    lines = raw.strip().split('\n')
    stats = {}
    pending_types = {}
    
    for line in lines[1:]:
        parts = line.split('\t')
        if len(parts) < 3:
            continue
        status, name, cnt = parts[0], parts[1], int(parts[2])
        if status not in stats:
            stats[status] = {'count': 0, 'types': {}}
        stats[status]['count'] += cnt
        stats[status]['types'][name] = cnt
    
    return stats

def main():
    ns = sys.argv[1] if len(sys.argv) > 1 else 'huadu'
    env = get_pod_env(ns)
    
    print(f"=== {ns} 队列统计 (DB) ===")
    
    db_raw = db_query(ns, env)
    if db_raw:
        stats = parse_db_output(db_raw)
        total = sum(s['count'] for s in stats.values())
        
        status_map = {'0': '待处理', '1': '处理中', '2': '已完成', '3': '异常/失败'}
        for key in ['0', '1', '2', '3']:
            if key in stats:
                label = status_map.get(key, f'status={key}')
                print(f"  {label}: {stats[key]['count']}")
                
                # Show top types for pending and failed
                if key in ('0', '3'):
                    top = sorted(stats[key]['types'].items(), key=lambda x: -x[1])[:5]
                    for name, cnt in top:
                        print(f"      {name}: {cnt}")
        
        print(f"  总计: {total}")
    
    # Redis supplement
    redis_out = redis_summary(ns, env)
    if redis_out:
        print(f"\nRedis 补充:")
        for line in redis_out.strip().split('\n'):
            print(f"  {line}")
    
    # Check if Redis and DB counts differ
    if db_raw and redis_out:
        db_pending = stats.get('0', {}).get('count', 0) + stats.get('1', {}).get('count', 0)
        import re
        m = re.search(r'Redis队列列表: (\d+)', redis_out)
        if m:
            redis_len = int(m.group(1))
            if abs(redis_len - db_pending) > 10:
                print(f"\n⚠️ 差异提示: DB 待处理+处理中({db_pending}) vs Redis 队列列表({redis_len})")

if __name__ == '__main__':
    main()
