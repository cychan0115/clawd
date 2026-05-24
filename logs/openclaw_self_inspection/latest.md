

---

## 异常深度分析

### 🔴 1. chrome-devtools MCP 启动失败 (持续性)

**状态**: 非致命但高频 — MCP最终能启动，但每次retry都失败

**现象**:
- 日志中频繁出现: `failed to start server "chrome-devtools" (npx -y chrome-devtools-mcp@latest --slim --headless): MCP error -32000: Connection closed`
- 覆盖 `openclaw-2026-05-25.log`, `openclaw-2026-05-24.log`, `gateway.err.log`
- gateway.err.log 共 98,147 行，末尾仍有此错误

**当前状态**: 
- ✅ chrome-devtools-mcp 实际在运行（2组进程，PID 91541/91542 和 94463/94473/94474）
- 版本 1.0.1

**根因推测**: MCP连接在初始化时超时/closed，OpenClaw自动retry后成功。可能与 `--slim --headless` 启动模式有关。

**建议**: 
- 若不影响使用，可忽略（最终能启动）
- 或考虑更新 chrome-devtools-mcp 到最新版本
- 或在 `openclaw.json` mcp.servers.chrome-devtools 中增加启动timeout

---

### 🔴 2. Gateway 内存压力告警 (需关注)

**状态**: 频繁触发

**现象**:
```
memory pressure: level=critical reason=heap_threshold 
  rssBytes=~2.8-2.9GB 
  heapUsedBytes=~2.1-2.4GB 
  thresholdBytes=2147483648 (2GB)
```

**当前状态**:
- Node进程总RSS: ~4.3GB
- macOS物理内存: 32GB，系统空闲88%
- 内存充足，但Node.js heap有默认限制

**根因**: Node.js V8引擎默认heap限制约2GB（64位系统会根据可用内存动态调整，但OpenClaw可能设置了固定阈值）。实际heap使用在2.1-2.4GB之间波动，超过2GB阈值触发告警。

**建议**: 
- 内存压力不影响功能，物理内存充足
- 可考虑增加 Node `--max-old-space-size` 参数（如4096）或调整 gateway 内存阈值配置
- 若出现OOM才需紧急处理

---

### 🟡 3. "主动发现-每2小时" cron job 持续失败 (需处理)

**状态**: 连续失败，已触发error backoff

**jobId**: `e3a596af-d4b9-40f1-ae36-d6208dc3e55b`

**现象**:
- 执行各种命令均失败：`run python3 scripts/task_state_manager.py`, `check git status`, `run df /`, `list files`, `edit .gitignore` 等
- 错误格式: `⚠️ 🛠️ \`command\` failed`
- 连续错误触发backoff: `consecutiveErrors:1, backoffMs:30000`

**根因分析**:
- 脚本文件本身正常（`task_state_manager.py` 存在且可执行）
- 在当前main session中exec工具正常工作
- **问题出在 cron isolated session 的 exec 工具权限/沙箱限制**
- 可能是isolated session缺少sandbox=inherit配置，或exec安全策略限制

**建议**:
- 检查该cron job的session配置，确认是否需要 `sandbox="inherit"`
- 或修改job payload避免需要exec工具的命令
- 这是一个已知模式问题，需要Anna review后决定修复方案

---

### 🟡 4. MiniMax MCP 未安装

**现象**: `uvx minimax-coding-plan-mcp -y ENOENT`

**根因**: `uvx` 未安装或 `minimax-coding-plan-mcp` 包不存在

**建议**: 
- 若不使用MiniMax模型，可忽略
- 或安装uvx: `pip install uv` 然后 `uv tool install minimax-coding-plan-mcp`

---

### 🟡 5. Data分区使用率 95%

**状态**: 需留意

```
/dev/disk3s5     460Gi   405Gi    26Gi    95%   /System/Volumes/Data
```

**说明**: 这是macOS的Data卷（用户数据分区）。当前使用率95%，剩余26GB。
- 短期内不会满
- 若持续增长，可能需要清理大文件

**建议**: 
- 可运行 `du -sh ~/* | sort -rh | head -20` 查找大文件夹
- 关注 `/Users/3pigcn` 下是否有日志/cache膨胀

---

### 🟢 6. 历史异常 (可忽略)

**gateway.err.log 中的旧记录**:
- 2026-01-27: homebrew tap `pimalaya/himalaya` git clone 404 失败
- curl 404 错误（同一时期）

这些是4个月前的历史残留，不影响当前系统运行。

---

### 🟢 7. 其他轻微异常

- **memos-cloud插件**: Auto-update failed (5月16日)，不影响功能
- **memory embeddings rate limited**: 偶尔出现，已自动retry
- **上次自巡检失败**: 因搜索日志命令失败，本次已成功

---

## 总结

| 优先级 | 问题 | 建议 |
|--------|------|------|
| 🔴 P1 | chrome-devtools MCP启动失败 | 可忽略（最终成功），或更新MCP版本 |
| 🔴 P1 | Gateway内存压力告警 | 可忽略（物理内存充足），关注是否OOM |
| 🟡 P2 | "主动发现" cron持续失败 | 需检查isolated session exec权限 |
| 🟡 P2 | Data分区95% | 定期关注，必要时清理 |
| 🟢 P3 | MiniMax MCP未安装 | 按需安装或忽略 |
| 🟢 P3 | 历史异常 | 已忽略 |

**整体评估**: MINI2 + OpenClaw 核心系统运行稳定。主要异常为非致命的间歇性问题（MCP启动retry、内存压力告警），不影响实际功能。唯一需要处理的cron job问题需要进一步诊断isolated session配置。

---
*深度分析完成 @ 2026-05-25 07:05*
