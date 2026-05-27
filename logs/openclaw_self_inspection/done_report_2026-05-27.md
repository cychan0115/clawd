# MINI2 + OpenClaw 自巡检结果

**时间**: 2026-05-27 13:30:17 (Asia/Shanghai)
**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`
**报告**: `/Users/3pigcn/clawd/logs/openclaw_self_inspection/latest.md`

---

## 检查项汇总

| 检查项 | 状态 |
|--------|------|
| macOS 主机负载 | ✅ 正常 (3.58/3.16/3.03) |
| macOS 内存压力 | ✅ 正常 (87% 空闲, 无 swap) |
| 主磁盘 (/) | ✅ 正常 (36% 使用率) |
| OpenClaw gateway 进程 | ✅ 运行中 |
| OpenClaw agent 进程 | ✅ 运行中 |
| OpenClaw browser 进程 | ✅ 运行中 |
| 端口 18789 | ✅ 监听中 |
| 端口 18800 | ✅ 监听中 |
| Gateway health | ✅ live |
| cron jobs.json | ✅ 正常 (16 jobs, 10 活跃) |
| 最近 cron runs | ✅ 正常 |

---

## 异常项

### ⚠️ 1. Gateway 日志异常

**`wing_recovery_alert.md` 编辑失败**
- 发现时间: 2026-05-26 及 2026-05-27
- 日志模式: `[tools] edit failed: Could not find the exact text in /Users/3pigcn/clawd/wing_recovery_alert.md`
- 影响: 可能导致相关任务（wing recovery alert）未能正确更新
- 建议: 需 Anna 检查 wing_recovery_alert.md 当前状态及编辑失败原因

**`chrome-devtools MCP server` 启动失败**
- 发现时间: 2026-05-26
- 日志模式: `failed to start server "chrome-devtools" (npx -y chrome-devtools-mcp@latest ...`
- 影响: MCP server 未启动，可能影响 browser devtools 集成
- 建议: 如持续失败需检查配置；单次失败可能为临时网络问题

### ⚠️ 2. Data 卷磁盘空间

- **使用率**: 95% (406Gi / 460Gi)
- **剩余**: 25Gi
- **影响**: 高使用率可能影响系统性能及大型文件写入
- **建议**: 系统巡检 cron (`078443c8-c048-4e69-8dab-eb99c185567b`) 已覆盖此项；如持续告警需手动清理

---

## 结论

**OpenClaw 核心服务全部正常** ✅
- gateway / agent / browser / cron 均运行正常
- 端口监听正常

**需要关注**: Gateway日志中的编辑失败异常建议 Anna 检查，确认是否影响 wing recovery alert 功能。

**无需 immediate action**: Data 卷空间由系统巡检独立处理。

---
*巡检完成 @ 2026-05-27 13:30*
