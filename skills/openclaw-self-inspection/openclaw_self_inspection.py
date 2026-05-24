#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenClaw + mini2 自巡检脚本
检查项：macOS 主机资源、磁盘、负载、OpenClaw 进程、端口、gateway 健康、cron 任务、日志
"""

import subprocess
import json
import os
import sys
import datetime
import re
from pathlib import Path

REPORT_DIR = Path("/Users/3pigcn/clawd/logs/openclaw_self_inspection")
REPORT_FILE = REPORT_DIR / "latest.md"
TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 颜色代码（终端输出用）
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def run_cmd(cmd, shell=False, timeout=30):
    """执行命令，返回 (returncode, stdout, stderr)"""
    try:
        if shell:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        else:
            result = subprocess.run(cmd, shell=False, capture_output=True, text=True, timeout=timeout)
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "Command timed out"
    except Exception as e:
        return -1, "", str(e)

def section(title):
    return f"\n## {title}\n"

def ok(text):
    return f"✅ {text}"

def warn(text):
    return f"⚠️ {text}"

def error(text):
    return f"❌ {text}"

def check_macos_resources():
    """检查 macOS 主机资源"""
    lines = [section("macOS 主机资源")]
    
    # CPU 负载
    rc, out, err = run_cmd(["uptime"])
    if rc == 0:
        lines.append(f"**负载**: `{out.strip()}`")
    else:
        lines.append(error(f"无法获取负载: {err}"))
    
    # 内存使用
    rc, out, err = run_cmd(["vm_stat"])
    if rc == 0:
        lines.append(f"**内存 (vm_stat)**:\n```\n{out}\n```")
    else:
        lines.append(error(f"无法获取内存: {err}"))
    
    # 活动内存压力
    rc, out, err = run_cmd(["memory_pressure"])
    if rc == 0:
        lines.append(f"**内存压力**:\n```\n{out}\n```")
    else:
        lines.append(error(f"无法获取内存压力: {err}"))
    
    return "\n".join(lines)

def check_disk():
    """检查磁盘"""
    lines = [section("磁盘空间")]
    
    rc, out, err = run_cmd(["df", "-h"])
    if rc == 0:
        lines.append(f"```\n{out}\n```")
    else:
        lines.append(error(f"无法获取磁盘信息: {err}"))
    
    # 检查主磁盘使用率
    rc, out, err = run_cmd(["df", "-h", "/"])
    if rc == 0:
        lines.append(f"**主磁盘 (/)**:\n```\n{out}\n```")
        # 解析使用率
        for line in out.splitlines():
            if line.startswith("/"):
                parts = line.split()
                if len(parts) >= 5:
                    usage_str = parts[4].replace('%', '')
                    try:
                        usage = int(usage_str)
                        if usage > 90:
                            lines.append(error(f"主磁盘使用率过高: {usage}%"))
                        elif usage > 80:
                            lines.append(warn(f"主磁盘使用率较高: {usage}%"))
                        else:
                            lines.append(ok(f"主磁盘使用率: {usage}%"))
                    except ValueError:
                        pass
    
    return "\n".join(lines)

def check_openclaw_processes():
    """检查 OpenClaw 相关进程"""
    lines = [section("OpenClaw 进程")]
    
    processes = {
        "gateway": ["openclaw", "gateway"],
        "agent": ["openclaw", "agent"],
        "browser": ["Chromium", "Chrome"],
    }
    
    for name, keywords in processes.items():
        rc, out, err = run_cmd(["pgrep", "-if", keywords[0]])
        if rc == 0 and out.strip():
            pids = out.strip().split()
            lines.append(ok(f"{name}: 运行中 (PIDs: {', '.join(pids)})"))
        else:
            # 尝试更宽泛的搜索
            rc2, out2, _ = run_cmd(["ps", "aux"])
            found = False
            if rc2 == 0:
                for line in out2.splitlines():
                    if any(k.lower() in line.lower() for k in keywords):
                        found = True
                        break
            if found:
                lines.append(ok(f"{name}: 运行中 (通过 ps 确认)"))
            else:
                lines.append(error(f"{name}: 未检测到运行进程"))
    
    return "\n".join(lines)

def check_ports():
    """检查端口 18789 和 18800"""
    lines = [section("端口监听")]
    
    for port in [18789, 18800]:
        rc, out, err = run_cmd(["lsof", "-i", f":{port}"])
        if rc == 0 and out.strip():
            lines.append(ok(f"端口 {port}: 监听中\n```\n{out}\n```"))
        else:
            rc2, out2, _ = run_cmd(["netstat", "-anv"])
            listening = False
            if rc2 == 0:
                for line in out2.splitlines():
                    if f".{port}" in line and ("LISTEN" in line or "listen" in line.lower()):
                        listening = True
                        break
            if listening:
                lines.append(ok(f"端口 {port}: 监听中 (通过 netstat 确认)"))
            else:
                lines.append(error(f"端口 {port}: 未检测到监听"))
    
    return "\n".join(lines)

def check_gateway_health():
    """检查 Gateway 健康状态"""
    lines = [section("Gateway 健康检查")]
    
    # 尝试本地健康检查
    rc, out, err = run_cmd(["curl", "-s", "http://localhost:18789/health"], timeout=10)
    if rc == 0:
        lines.append(ok(f"Gateway health: {out.strip()}"))
    else:
        lines.append(warn(f"Gateway health 检查失败 (curl rc={rc}): {err}"))
    
    # 检查 gateway 版本
    rc, out, err = run_cmd(["openclaw", "gateway", "status"], timeout=10)
    if rc == 0:
        lines.append(ok(f"Gateway status:\n```\n{out}\n```"))
    else:
        lines.append(warn(f"`openclaw gateway status` 失败: {err}"))
    
    return "\n".join(lines)

def check_cron_jobs():
    """检查 cron jobs"""
    lines = [section("Cron Jobs")]
    
    jobs_file = Path(os.path.expanduser("~/.openclaw/cron/jobs.json"))
    if jobs_file.exists():
        try:
            with open(jobs_file) as f:
                data = json.load(f)
            jobs = data.get("jobs", data) if isinstance(data, dict) else data
            lines.append(ok(f"jobs.json: 存在 ({len(jobs)} 个 job)"))
            # 列出活跃任务
            active = [j for j in jobs if j.get("enabled", True)]
            lines.append(f"活跃任务: {len(active)} 个")
            for j in active[:5]:  # 只显示前5个
                name = j.get("name", "unnamed")
                schedule = j.get("schedule", {})
                lines.append(f"- `{name}`: {schedule}")
        except Exception as e:
            lines.append(error(f"解析 jobs.json 失败: {e}"))
    else:
        lines.append(warn(f"jobs.json 不存在: {jobs_file}"))
    
    return "\n".join(lines)

def check_cron_runs():
    """检查最近的 cron runs"""
    lines = [section("最近 Cron Runs")]
    
    runs_dir = Path(os.path.expanduser("~/.openclaw/cron/runs"))
    if runs_dir.exists():
        try:
            files = sorted(runs_dir.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
            recent = files[:10]
            lines.append(f"最近 {len(recent)} 次运行记录:")
            for f in recent:
                mtime = datetime.datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                lines.append(f"- `{f.name}` (更新时间: {mtime})")
        except Exception as e:
            lines.append(error(f"读取 runs 目录失败: {e}"))
    else:
        lines.append(warn(f"runs 目录不存在: {runs_dir}"))
    
    return "\n".join(lines)

def check_gateway_logs():
    """检查 gateway 日志中的异常"""
    lines = [section("Gateway 日志异常")]
    
    log_dirs = [
        Path(os.path.expanduser("~/.openclaw/logs")),
        Path("/tmp/openclaw"),
    ]
    
    errors_found = False
    for log_dir in log_dirs:
        if not log_dir.exists():
            continue
        # 查找最近的日志文件
        log_files = sorted(
            [f for f in log_dir.iterdir() if f.is_file() and f.suffix in ('.log', '.txt', '')],
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )
        for log_file in log_files[:3]:
            try:
                with open(log_file, 'r', errors='ignore') as f:
                    content = f.read(50000)  # 只读前50KB
                # 搜索错误关键词
                error_patterns = ['error', 'fatal', 'panic', 'crash', 'exception']
                found_errors = []
                for pat in error_patterns:
                    matches = re.findall(f'.*{pat}.*', content, re.IGNORECASE)
                    if matches:
                        found_errors.extend(matches[-3:])  # 最近3条
                if found_errors:
                    errors_found = True
                    lines.append(warn(f"`{log_file.name}` 中发现异常:"))
                    for e in found_errors[:5]:
                        lines.append(f"  - `{e.strip()[:120]}`")
            except Exception:
                pass
    
    if not errors_found:
        lines.append(ok("最近日志中未检测到明显异常"))
    
    return "\n".join(lines)

def check_system_load():
    """检查系统整体负载"""
    lines = [section("系统整体状态")]
    
    # top 输出
    rc, out, err = run_cmd(["top", "-l", "1", "-n", "10"], timeout=15)
    if rc == 0:
        lines.append(f"**Top 进程**:\n```\n{out[:2000]}\n```")
    else:
        lines.append(warn(f"top 命令失败: {err}"))
    
    return "\n".join(lines)

def generate_report():
    """生成完整报告"""
    report_parts = [
        f"# MINI2 + OpenClaw 自巡检报告\n",
        f"**时间**: {TIMESTAMP} (Asia/Shanghai)\n",
        f"**主机**: mini2 (Mac mini)\n",
        f"**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`\n",
    ]
    
    checks = [
        check_macos_resources,
        check_disk,
        check_openclaw_processes,
        check_ports,
        check_gateway_health,
        check_cron_jobs,
        check_cron_runs,
        check_gateway_logs,
        check_system_load,
    ]
    
    for check_fn in checks:
        try:
            report_parts.append(check_fn())
        except Exception as e:
            report_parts.append(f"\n## {check_fn.__name__}\n❌ 检查异常: {e}\n")
    
    report_parts.append(f"\n---\n*报告生成完成 @ {TIMESTAMP}*\n")
    return "\n".join(report_parts)

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    
    print(f"[{TIMESTAMP}] 开始 OpenClaw 自巡检...")
    report = generate_report()
    
    # 写入报告
    with open(REPORT_FILE, 'w') as f:
        f.write(report)
    
    print(f"报告已写入: {REPORT_FILE}")
    
    # 判断是否有异常
    if "❌" in report or "⚠️" in report:
        print("\n" + "="*50)
        print("发现异常项，请查看报告!")
        print("="*50)
        # 在终端打印异常部分
        for line in report.splitlines():
            if line.startswith("❌") or line.startswith("⚠️"):
                print(line)
        return 1
    else:
        print("\n✅ 所有检查项正常")
        return 0

if __name__ == "__main__":
    sys.exit(main())
