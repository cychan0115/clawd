
## 巡检结论与建议

**时间**: 2026-05-25 10:30 (Asia/Shanghai)

### 整体状态: 🟡 有异常，但系统正常运行

| 检查项 | 状态 |
|---|---|
| macOS 主机资源 | ✅ 正常 (负载 2.8, 内存 53% 空闲, 无 swap) |
| 磁盘空间 | ✅ 正常 (主磁盘 33%, Data 卷 94% 为 macOS 正常状态) |
| OpenClaw Gateway | ✅ 运行中 (PID 71611, health: live) |
| OpenClaw Agent | ✅ 运行中 |
| OpenClaw Browser | ✅ 运行中 |
| 端口 18789 | ✅ 监听中 |
| 端口 18800 | ✅ 监听中 |
| Cron Jobs | ✅ 16 个任务配置正常, 10 个活跃 |

### 异常项分析

**1. ⚠️ chrome-devtools MCP 启动失败 (5/25 日志中出现多次)**
- **当前状态**: ✅ MCP 已成功运行 (PID 13167, 10:30 启动)
- **原因**: 启动过程中 bundle-tools 阶段 (~30s) 有重试，超时/连接关闭后自动重试成功
- **关联**: 与 gateway 内存压力有关
- **建议**: 持续观察，如频繁发生可考虑增加 gateway 内存限制或调整 MCP 超时

**2. ⚠️ Gateway 内存压力频繁达到 critical (今天 280 次)**
- **详情**: heapUsed 2.1-2.7GB, 超过 2.1GB threshold
- **影响**: 系统整体稳定，无 swap 使用，但可能导致 MCP 启动变慢
- **建议**: 
  - 考虑在 `~/.openclaw/openclaw.json` 中增加 heap 限制
  - 或启用 `diagnostics.memoryPressureSnapshot` 帮助诊断

**3. ⚠️ Cron job "主动发现-每2小时" (e3a596af) 最近执行失败**
- **错误**: `check git status (in ~/clawd)` failed
- **可能原因**: agent 尝试使用 `host=sandbox` 但 gateway 未启用 sandbox 模式
- **建议**: 检查该 job 的配置，确认是否需要 sandbox 或改为 host=auto/gateway

**4. ⚠️ gateway.err.log 中的旧错误**
- **详情**: 2026-01-27 的 homebrew tap 克隆失败
- **建议**: 历史遗留，无需处理

### 建议行动（优先级排序）

1. **低优先级**: 调查 cron job `e3a596af` 的 sandbox 配置问题
2. **低优先级**: 评估是否增加 gateway 内存限制以减少 pressure 警告
3. **无需行动**: chrome-devtools MCP 已自动恢复, homebrew 旧错误忽略

---
*巡检完成 @ 2026-05-25 10:30:11*
