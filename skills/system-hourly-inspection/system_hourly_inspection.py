#!/usr/bin/env python3
"""
System Hourly Inspection

Checks:
- K8S: abnormal pods, restarts, error logs
- Host: CPU, memory, disk, load
- HTTP endpoints: accessibility and response time

Sends email alert only when anomalies are found.
"""

import os
import sys
import json
import subprocess
import smtplib
import urllib.request
import urllib.error
import ssl
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load .env from memory/ (persistent location, survives skill updates)
env_path = os.path.join(os.path.expanduser('~/clawd/memory'), 'system_hourly_inspection.env')
load_dotenv(env_path)


class SystemInspection:
    def __init__(self):
        self.http_endpoints = self._parse_endpoints(os.getenv('HTTP_ENDPOINTS', ''))
        self.smtp_host = os.getenv('SMTP_HOST', 'smtp.139.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', '25'))
        self.smtp_user = os.getenv('SMTP_USER', '13926262295@139.com')
        self.smtp_pass = os.getenv('SMTP_PASS', '')
        self.alert_recipient = os.getenv('ALERT_RECIPIENT', '13926262295@139.com')
        self.k8s_context = os.getenv('K8S_CONTEXT', '')
        self.cpu_threshold = int(os.getenv('CPU_THRESHOLD', '80'))
        self.mem_threshold = int(os.getenv('MEM_THRESHOLD', '80'))
        self.disk_threshold = int(os.getenv('DISK_THRESHOLD', '85'))
        self.load_threshold = float(os.getenv('LOAD_THRESHOLD', '5.0'))
        
        self.findings = []
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    def _parse_endpoints(self, raw):
        if not raw:
            return []
        return [u.strip() for u in raw.split(',') if u.strip()]
    
    def _run_cmd(self, cmd, timeout=30):
        """Run shell command and return (stdout, stderr, rc)"""
        try:
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=timeout
            )
            return result.stdout.strip(), result.stderr.strip(), result.returncode
        except subprocess.TimeoutExpired:
            return '', 'Command timed out', -1
        except Exception as e:
            return '', str(e), -1
    
    def _add_finding(self, category, severity, title, detail):
        self.findings.append({
            'category': category,
            'severity': severity,
            'title': title,
            'detail': detail,
        })
    
    def check_k8s(self):
        """Check K8S cluster status"""
        print('\n🔍 Checking K8S...')
        
        # Check kubectl connectivity
        ctx_flag = f' --context={self.k8s_context}' if self.k8s_context else ''
        _, err, rc = self._run_cmd(f'kubectl{ctx_flag} cluster-info', timeout=10)
        if rc != 0:
            if 'connection refused' in err.lower() or 'unable to connect' in err.lower() or 'the server' in err.lower():
                self._add_finding('K8S', 'WARNING', 'K8S Cluster Unreachable', err or 'Cannot connect to K8S cluster')
                print('  ⚠️ K8S cluster unreachable')
                return
            # Try minikube
            out, err2, rc2 = self._run_cmd('minikube status', timeout=10)
            if rc2 != 0 or 'Running' not in out:
                self._add_finding('K8S', 'INFO', 'K8S Not Available', 'No active K8S cluster found (kubectl or minikube)')
                print('  ℹ️ K8S not available')
                return
        
        # Check abnormal pods
        out, err, rc = self._run_cmd(
            f"kubectl{ctx_flag} get pods --all-namespaces --field-selector=status.phase!=Succeeded,status.phase!=Running -o json",
            timeout=15
        )
        if rc == 0:
            try:
                data = json.loads(out)
                items = data.get('items', [])
                if items:
                    pods_info = []
                    for pod in items[:10]:
                        ns = pod['metadata']['namespace']
                        name = pod['metadata']['name']
                        phase = pod['status']['phase']
                        pods_info.append(f"{ns}/{name}: {phase}")
                    self._add_finding('K8S', 'ERROR', f'Abnormal Pods: {len(items)}', '\n'.join(pods_info))
                    print(f'  ❌ {len(items)} abnormal pods')
                else:
                    print('  ✅ All pods running')
            except json.JSONDecodeError:
                pass
        
        # Check pods with high restart counts
        out, err, rc = self._run_cmd(
            f"kubectl{ctx_flag} get pods --all-namespaces -o json",
            timeout=15
        )
        if rc == 0:
            try:
                data = json.loads(out)
                high_restart = []
                for pod in data.get('items', []):
                    restart_count = 0
                    for cs in pod.get('status', {}).get('containerStatuses', []):
                        restart_count = max(restart_count, cs.get('restartCount', 0))
                    if restart_count >= 5:
                        ns = pod['metadata']['namespace']
                        name = pod['metadata']['name']
                        high_restart.append(f"{ns}/{name}: {restart_count} restarts")
                if high_restart:
                    self._add_finding('K8S', 'WARNING', f'High Restart Pods: {len(high_restart)}', '\n'.join(high_restart[:10]))
                    print(f'  ⚠️ {len(high_restart)} pods with high restarts')
            except json.JSONDecodeError:
                pass
        
        # Check recent error logs (last 5 minutes)
        out, err, rc = self._run_cmd(
            f"kubectl{ctx_flag} logs --all-containers --since=5m --selector='' --all-namespaces 2>/dev/null | grep -iE '(error|fatal|exception|crash|failed|panic)' | head -20",
            timeout=15
        )
        if rc == 0 and out:
            lines = out.split('\n')[:20]
            self._add_finding('K8S', 'ERROR', 'Recent Error Logs', '\n'.join(lines))
            print(f'  ❌ Found {len(lines)} error log lines')
        
        # Check node status
        out, err, rc = self._run_cmd(
            f"kubectl{ctx_flag} get nodes -o json",
            timeout=10
        )
        if rc == 0:
            try:
                data = json.loads(out)
                not_ready = []
                for node in data.get('items', []):
                    name = node['metadata']['name']
                    for cond in node.get('status', {}).get('conditions', []):
                        if cond.get('type') == 'Ready' and cond.get('status') != 'True':
                            not_ready.append(f"{name}: {cond.get('reason', 'NotReady')}")
                if not_ready:
                    self._add_finding('K8S', 'CRITICAL', 'Nodes Not Ready', '\n'.join(not_ready))
                    print(f'  🔴 {len(not_ready)} nodes not ready')
            except json.JSONDecodeError:
                pass
    
    def check_host_resources(self):
        """Check host CPU, memory, disk, load"""
        print('\n🔍 Checking Host Resources...')
        
        # CPU usage (macOS: top -l 1 | grep "CPU usage")
        out, _, rc = self._run_cmd("top -l 1 -n 0 | grep 'CPU usage' | head -1")
        if rc == 0 and out:
            # Parse: "CPU usage: 10.34% user, 8.90% sys, 80.75% idle"
            import re
            user_sys = re.findall(r'(\d+\.?\d*)%\s+(?:user|sys)', out)
            total_cpu = sum(float(x) for x in user_sys) if user_sys else 0
            if total_cpu > self.cpu_threshold:
                self._add_finding('HOST', 'WARNING', f'High CPU Usage: {total_cpu:.1f}%', out)
                print(f'  ⚠️ CPU {total_cpu:.1f}%')
            else:
                print(f'  ✅ CPU {total_cpu:.1f}%')
        
        # Memory (macOS: vm_stat + sysctl)
        out, _, rc = self._run_cmd("sysctl hw.memsize | awk '{print $2}'")
        if rc == 0:
            total_mem = int(out) / (1024**3)  # GB
            out2, _, rc2 = self._run_cmd("vm_stat | grep 'Pages free' | awk '{print $3}' | tr -d '.'")
            if rc2 == 0:
                try:
                    page_size = 4096  # macOS default
                    free_pages = int(out2)
                    free_mem = (free_pages * page_size) / (1024**3)
                    used_mem = total_mem - free_mem
                    mem_pct = (used_mem / total_mem) * 100 if total_mem > 0 else 0
                    if mem_pct > self.mem_threshold:
                        self._add_finding('HOST', 'WARNING', f'High Memory Usage: {mem_pct:.1f}%', f'Used: {used_mem:.1f}GB / {total_mem:.1f}GB')
                        print(f'  ⚠️ Memory {mem_pct:.1f}%')
                    else:
                        print(f'  ✅ Memory {mem_pct:.1f}%')
                except ValueError:
                    pass
        
        # Disk usage
        out, _, rc = self._run_cmd("df -h / | tail -1 | awk '{print $5}' | tr -d '%'")
        if rc == 0:
            try:
                disk_pct = int(out)
                if disk_pct > self.disk_threshold:
                    self._add_finding('HOST', 'ERROR', f'High Disk Usage: {disk_pct}%', f'Root filesystem at {disk_pct}% capacity')
                    print(f'  ❌ Disk {disk_pct}%')
                else:
                    print(f'  ✅ Disk {disk_pct}%')
            except ValueError:
                pass
        
        # Load average
        out, _, rc = self._run_cmd("uptime | awk -F'load averages:' '{print $2}' | awk '{print $1}' | tr -d ','")
        if rc == 0:
            try:
                load = float(out)
                if load > self.load_threshold:
                    self._add_finding('HOST', 'WARNING', f'High Load Average: {load}', f'System load: {load} (threshold: {self.load_threshold})')
                    print(f'  ⚠️ Load {load}')
                else:
                    print(f'  ✅ Load {load}')
            except ValueError:
                pass
        
        # Docker status
        out, err, rc = self._run_cmd("docker info --format '{{.ServerVersion}}' 2>/dev/null")
        if rc != 0:
            self._add_finding('HOST', 'WARNING', 'Docker Not Running', err or 'Docker daemon is not accessible')
            print('  ⚠️ Docker not running')
        else:
            print('  ✅ Docker running')
    
    def check_http_endpoints(self):
        """Check HTTP endpoints"""
        print('\n🔍 Checking HTTP Endpoints...')
        
        if not self.http_endpoints:
            print('  ℹ️ No HTTP endpoints configured')
            return
        
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        for url in self.http_endpoints:
            try:
                start = datetime.now()
                req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'OpenClaw-HealthCheck/1.0'})
                resp = urllib.request.urlopen(req, timeout=10, context=ctx)
                elapsed = (datetime.now() - start).total_seconds()
                status = resp.status
                if status >= 400:
                    self._add_finding('HTTP', 'ERROR', f'HTTP {status}: {url}', f'Response time: {elapsed:.2f}s, Status: {status}')
                    print(f'  ❌ {url} -> {status} ({elapsed:.2f}s)')
                elif elapsed > 5:
                    self._add_finding('HTTP', 'WARNING', f'Slow Response: {url}', f'Response time: {elapsed:.2f}s, Status: {status}')
                    print(f'  ⚠️ {url} -> {status} ({elapsed:.2f}s)')
                else:
                    print(f'  ✅ {url} -> {status} ({elapsed:.2f}s)')
            except urllib.error.HTTPError as e:
                self._add_finding('HTTP', 'ERROR', f'HTTP {e.code}: {url}', str(e.reason))
                print(f'  ❌ {url} -> {e.code}')
            except Exception as e:
                self._add_finding('HTTP', 'ERROR', f'HTTP Unreachable: {url}', str(e))
                print(f'  ❌ {url} -> Unreachable ({e})')
    
    def generate_report(self):
        """Generate inspection report"""
        lines = [
            f'# 🚨 System Inspection Report',
            f'**Time:** {self.timestamp} (Asia/Shanghai)',
            f'**Host:** mini2 (Mac mini)',
            '',
        ]
        
        if not self.findings:
            lines.extend([
                '## ✅ All Clear',
                '',
                'No anomalies detected in this inspection.',
            ])
        else:
            # Group by severity
            severity_order = ['CRITICAL', 'ERROR', 'WARNING', 'INFO']
            severity_emoji = {'CRITICAL': '🔴', 'ERROR': '❌', 'WARNING': '⚠️', 'INFO': 'ℹ️'}
            
            lines.append(f'## 📊 Summary: {len(self.findings)} finding(s)')
            lines.append('')
            
            for sev in severity_order:
                items = [f for f in self.findings if f['severity'] == sev]
                if items:
                    lines.append(f'### {severity_emoji.get(sev, "•")} {sev} ({len(items)})')
                    lines.append('')
                    for item in items:
                        lines.append(f'**[{item["category"]}] {item["title"]}**')
                        lines.append(f'```')
                        lines.append(item['detail'])
                        lines.append(f'```')
                        lines.append('')
        
        lines.extend([
            '---',
            '_Generated by OpenClaw System Hourly Inspection_',
        ])
        
        return '\n'.join(lines)
    
    def send_email_alert(self, report):
        """Send email alert if findings exist and SMTP is configured"""
        if not self.findings:
            print('\n✅ No anomalies. No email sent.')
            return True
        
        if not self.smtp_pass:
            print('\n⚠️ SMTP password not configured. Email not sent.')
            print('Set SMTP_PASS in .env to enable email alerts.')
            return False
        
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f'🚨 System Alert: {len(self.findings)} finding(s) at {self.timestamp}'
            msg['From'] = self.smtp_user
            msg['To'] = self.alert_recipient
            
            # Plain text version
            plain = report.replace('# ', '').replace('**', '').replace('```', '')
            msg.attach(MIMEText(plain, 'plain', 'utf-8'))
            msg.attach(MIMEText(report, 'html', 'utf-8'))
            
            # Use HTML wrapper for markdown-like formatting
            html_body = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; line-height: 1.6; max-width: 800px; margin: 20px auto; padding: 20px; }}
h1 {{ color: #d32f2f; }}
h2 {{ color: #333; border-bottom: 1px solid #eee; padding-bottom: 8px; }}
h3 {{ color: #555; }}
pre {{ background: #f5f5f5; padding: 12px; border-radius: 4px; overflow-x: auto; }}
.error {{ color: #d32f2f; }}
.warning {{ color: #f57c00; }}
.success {{ color: #388e3c; }}
hr {{ border: none; border-top: 1px solid #eee; margin: 20px 0; }}
</style>
</head>
<body>
{self._markdown_to_html(report)}
</body>
</html>"""
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f'🚨 System Alert: {len(self.findings)} finding(s) at {self.timestamp}'
            msg['From'] = self.smtp_user
            msg['To'] = self.alert_recipient
            msg.attach(MIMEText(plain, 'plain', 'utf-8'))
            msg.attach(MIMEText(html_body, 'html', 'utf-8'))
            
            with smtplib.SMTP(self.smtp_host, self.smtp_port, timeout=30) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_pass)
                server.sendmail(self.smtp_user, [self.alert_recipient], msg.as_string())
            
            print(f'\n📧 Alert email sent to {self.alert_recipient}')
            return True
            
        except Exception as e:
            print(f'\n❌ Failed to send email: {e}')
            return False
    
    def _markdown_to_html(self, md):
        """Simple markdown to HTML conversion"""
        lines = md.split('\n')
        html = []
        in_pre = False
        pre_content = []
        
        for line in lines:
            if line.startswith('# '):
                if in_pre:
                    html.append('<pre>' + '\n'.join(pre_content) + '</pre>')
                    in_pre = False
                    pre_content = []
                html.append(f'<h1>{line[2:]}</h1>')
            elif line.startswith('## '):
                if in_pre:
                    html.append('<pre>' + '\n'.join(pre_content) + '</pre>')
                    in_pre = False
                    pre_content = []
                html.append(f'<h2>{line[3:]}</h2>')
            elif line.startswith('### '):
                if in_pre:
                    html.append('<pre>' + '\n'.join(pre_content) + '</pre>')
                    in_pre = False
                    pre_content = []
                html.append(f'<h3>{line[4:]}</h3>')
            elif line.startswith('**') and line.endswith('**'):
                if in_pre:
                    html.append('<pre>' + '\n'.join(pre_content) + '</pre>')
                    in_pre = False
                    pre_content = []
                html.append(f'<p><strong>{line[2:-2]}</strong></p>')
            elif line == '```':
                if in_pre:
                    html.append('<pre>' + '\n'.join(pre_content) + '</pre>')
                    in_pre = False
                    pre_content = []
                else:
                    in_pre = True
            elif in_pre:
                pre_content.append(line)
            elif line.startswith('---'):
                html.append('<hr>')
            elif line.strip():
                html.append(f'<p>{line}</p>')
        
        if in_pre:
            html.append('<pre>' + '\n'.join(pre_content) + '</pre>')
        
        return '\n'.join(html)
    
    def save_report(self, report):
        """Save report to memory directory"""
        today = datetime.now().strftime('%Y-%m-%d')
        output_dir = os.path.expanduser('~/clawd/memory')
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"{output_dir}/system_inspection_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f'\n💾 Report saved to: {filename}')
        return filename
    
    def run(self):
        """Main execution"""
        print('=' * 60)
        print(f'🤖 System Hourly Inspection — {self.timestamp}')
        print('=' * 60)
        
        self.check_k8s()
        self.check_host_resources()
        self.check_http_endpoints()
        
        report = self.generate_report()
        
        print('\n' + '=' * 60)
        print(report)
        print('=' * 60)
        
        self.save_report(report)
        self.send_email_alert(report)
        
        print(f'\n✅ Inspection complete: {len(self.findings)} finding(s)')


if __name__ == '__main__':
    inspector = SystemInspection()
    inspector.run()
