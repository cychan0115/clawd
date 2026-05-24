# System Hourly Inspection Skill

每小时系统巡检，自动检查 K8S、主机资源和 HTTP 端点，异常时发送邮件报告。

## 功能

- **K8S 日志检查**：异常 Pod 状态、重启次数、错误日志
- **主机资源检查**：CPU、内存、磁盘、负载
- **HTTP 端点检查**：配置 URL 的可访问性
- **异常邮件报告**：仅在有异常时发送

## 配置

复制 `.env.example` 为 `.env` 并填写：

```bash
cp .env.example .env
```

## 运行

```bash
python3 system_hourly_inspection.py
```

## Cron 配置

每小时执行一次：

```
0 * * * * cd /Users/3pigcn/clawd/skills/system-hourly-inspection && /opt/homebrew/bin/python3 system_hourly_inspection.py >> /tmp/system_hourly_inspection.log 2>&1
```
