#!/usr/bin/env python3
"""JYH Queue Inspector — fast queue count check."""
import sys, subprocess, os, json

CACHE_DIR = os.path.expanduser("~/.cache/jyh-queue-inspector")

def run_on_ocr1(cmd, timeout=15):
    r = subprocess.run(f"ssh ocr1 '{cmd}'", shell=True, capture_output=True, text=True, timeout=timeout)
    return r.stdout.strip(), r.stderr.strip(), r.returncode

def get_cached_env(ns):
    cache_file = os.path.join(CACHE_DIR, f"{ns}_env.json")
    if os.path.exists(cache_file):
        with open(cache_file) as f:
            return json.load(f)
    return None

def save_cached_env(ns, env):
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_file = os.path.join(CACHE_DIR, f"{ns}_env.json")
    with open(cache_file, 'w') as f:
        json.dump(env, f)

def get_env(ns):
    env = get_cached_env(ns)
    if env:
        return env
    
    out, err, rc = run_on_ocr1(f"kubectl get pods -n {ns} -o jsonpath='{{.items[0].metadata.name}}'")
    if rc != 0:
        print(f"Failed: {err}")
        sys.exit(1)
    pod = out.strip()
    
    out, err, rc = run_on_ocr1(f"kubectl exec -n {ns} {pod} -- env | grep -E 'DB_HOST|DB_PORT|DB_USER|DB_PASSWORD|DB_NAME'")
    env = {}
    for line in out.strip().split('\n'):
        if '=' in line:
            k, v = line.split('=', 1)
            env[k] = v
    
    save_cached_env(ns, env)
    return env

def fast_query(ns, env):
    host = env.get('DB_HOST', '')
    port = env.get('DB_PORT', '3306')
    user = env.get('DB_USER', 'root')
    password = env.get('DB_PASSWORD', '')
    dbname = env.get('DB_NAME', '')
    
    sql = "SELECT status, COUNT(*) FROM queue GROUP BY status;"
    cmd = f"mysql -h {host} -P {port} -u {user} -p'{password}' -D {dbname} -e \"{sql}\""
    out, err, rc = run_on_ocr1(cmd, timeout=10)
    if rc != 0:
        print(f"DB error: {err[:200]}")
        return None
    return out

def detail_query(ns, env):
    host = env.get('DB_HOST', '')
    port = env.get('DB_PORT', '3306')
    user = env.get('DB_USER', 'root')
    password = env.get('DB_PASSWORD', '')
    dbname = env.get('DB_NAME', '')
    
    sql = "SELECT status, name, COUNT(*) FROM queue GROUP BY status, name ORDER BY status, COUNT(*) DESC;"
    cmd = f"mysql -h {host} -P {port} -u {user} -p'{password}' -D {dbname} -e \"{sql}\""
    out, err, rc = run_on_ocr1(cmd, timeout=15)
    if rc != 0:
        return None
    return out

def main():
    detail = '--detail' in sys.argv
    ns = [a for a in sys.argv[1:] if not a.startswith('--')][0] if [a for a in sys.argv[1:] if not a.startswith('--')] else 'huadu'
    
    env = get_env(ns)
    
    print(f"=== {ns} 队列 ===")
    
    out = fast_query(ns, env)
    if not out:
        return
    
    status_map = {'0': '待处理', '1': '处理中', '2': '已完成', '3': '异常/失败'}
    total = 0
    lines = out.strip().split('\n')[1:]
    
    for line in lines:
        parts = line.split('\t')
        if len(parts) >= 2:
            status, cnt = parts[0], int(parts[1])
            label = status_map.get(status, f'status={status}')
            print(f"{label}: {cnt}")
            total += cnt
    
    print(f"总计: {total}")
    
    if detail:
        print("\n--- 明细 ---")
        d = detail_query(ns, env)
        if d:
            for line in d.strip().split('\n')[1:]:
                parts = line.split('\t')
                if len(parts) >= 3:
                    print(f"  [{parts[0]}] {parts[1]}: {parts[2]}")

if __name__ == '__main__':
    main()
