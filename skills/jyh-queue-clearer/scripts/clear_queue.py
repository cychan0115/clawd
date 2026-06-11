#!/usr/bin/env python3
"""JYH Queue Clearer — cancel pending queue tasks by marking them done."""
import sys, subprocess, argparse

def run_on_ocr1(cmd, timeout=15):
    r = subprocess.run(f"ssh ocr1 '{cmd}'", shell=True, capture_output=True, text=True, timeout=timeout)
    return r.stdout.strip(), r.stderr.strip(), r.returncode

def get_pod_env(ns):
    out, err, rc = run_on_ocr1(f"kubectl get pods -n {ns} -o jsonpath='{{.items[0].metadata.name}}'")
    if rc != 0:
        print(f"Failed to get pod: {err}")
        return {}
    pod = out.strip()
    out, err, rc = run_on_ocr1(f"kubectl exec -n {ns} {pod} -- env | grep -E 'DB_HOST|DB_PORT|DB_USER|DB_PASSWORD|DB_NAME'")
    env = {}
    for line in out.strip().split('\n'):
        if '=' in line:
            k, v = line.split('=', 1)
            env[k] = v
    return env

def preview(ns, env):
    host = env.get('DB_HOST', '')
    port = env.get('DB_PORT', '3306')
    user = env.get('DB_USER', 'root')
    password = env.get('DB_PASSWORD', '')
    dbname = env.get('DB_NAME', '')
    
    sql = "SELECT status, name, COUNT(*) as cnt FROM queue WHERE status IN (0, 1) GROUP BY status, name ORDER BY status, cnt DESC;"
    cmd = f"mysql -h {host} -P {port} -u {user} -p'{password}' -D {dbname} -e \"{sql}\""
    out, err, rc = run_on_ocr1(cmd, timeout=30)
    if rc != 0:
        print(f"DB query failed: {err[:200]}")
        return None
    
    lines = out.strip().split('\n')
    total = 0
    print(f"=== {ns} 待取消队列预览 ===")
    for line in lines[1:]:
        parts = line.split('\t')
        if len(parts) >= 3:
            status, name, cnt = parts[0], parts[1], parts[2]
            total += int(cnt)
            print(f"  status={status} {name}: {cnt}")
    print(f"\n总计待取消: {total}")
    return total

def execute(ns, env):
    host = env.get('DB_HOST', '')
    port = env.get('DB_PORT', '3306')
    user = env.get('DB_USER', 'root')
    password = env.get('DB_PASSWORD', '')
    dbname = env.get('DB_NAME', '')
    
    sql = """UPDATE queue SET status = 2, update_time = NOW(6) WHERE status IN (0, 1);"""
    cmd = f"mysql -h {host} -P {port} -u {user} -p'{password}' -D {dbname} -e \"{sql}\""
    out, err, rc = run_on_ocr1(cmd, timeout=60)
    if rc != 0:
        print(f"UPDATE failed: {err[:200]}")
        return False
    
    # Check affected rows from output
    print(f"执行结果: {out}")
    
    # Verify
    verify_sql = "SELECT status, COUNT(*) as cnt FROM queue GROUP BY status;"
    cmd = f"mysql -h {host} -P {port} -u {user} -p'{password}' -D {dbname} -e \"{verify_sql}\""
    out, err, rc = run_on_ocr1(cmd, timeout=30)
    if rc == 0:
        print(f"\n=== 验证结果 ===")
        for line in out.strip().split('\n')[1:]:
            parts = line.split('\t')
            if len(parts) >= 2:
                status_map = {'0': '待处理', '1': '处理中', '2': '已完成', '3': '异常/失败'}
                status = status_map.get(parts[0], f"status={parts[0]}")
                print(f"  {status}: {parts[1]}")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('namespace', default='huadu', nargs='?')
    parser.add_argument('--preview', action='store_true', help='Preview only, do not execute')
    parser.add_argument('--execute', action='store_true', help='Execute update after confirmation')
    args = parser.parse_args()
    
    env = get_pod_env(args.namespace)
    if not env:
        sys.exit(1)
    
    total = preview(args.namespace, env)
    if total is None or total == 0:
        print("无待取消队列")
        return
    
    if args.preview:
        print("\n预览模式，未执行任何操作。如需执行请加 --execute")
        return
    
    if args.execute:
        print(f"\n正在执行取消...")
        execute(args.namespace, env)
    else:
        print(f"\n请确认: 是否将 {total} 个待处理/处理中队列标记为完成?")
        print("回复 --execute 参数执行，或加 --preview 仅预览")

if __name__ == '__main__':
    main()
