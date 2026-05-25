# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-25 10:00:12 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `10:00  up 7 days, 12:52, 7 users, load averages: 3.10 3.23 3.11`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                                4030.
Pages active:                            659884.
Pages inactive:                          657994.
Pages speculative:                         1275.
Pages throttled:                              0.
Pages wired down:                        548932.
Pages purgeable:                          23932.
"Translation faults":                5604447512.
Pages copy-on-write:                  160376160.
Pages zero filled:                   3737040807.
Pages reactivated:                     16846143.
Pages purged:                           2041163.
File-backed pages:                       458594.
Anonymous pages:                         860559.
Pages stored in compressor:              378553.
Pages occupied by compressor:            190464.
Decompressions:                         5495590.
Compressions:                          12787809.
Pageins:                               40186066.
Pageouts:                                988802.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 3614 
Pages purgeable: 23927 
Pages purged: 2041165 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 659885 
Pages inactive: 657930 
Pages speculative: 1280 
Pages throttled: 0 
Pages wired down: 548936 

Compressor Stats:
Pages used by compressor: 190488 
Pages decompressed: 5495590 
Pages compressed: 12787925 

File I/O:
Pageins: 40186067 
Pageouts: 988802 

System-wide memory free percentage: 64%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    26Gi    35%    426k  271M    0%   /
devfs            201Ki   201Ki     0Bi   100%     696     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    26Gi     1%       0  271M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    26Gi    34%    1.8k  271M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    26Gi     3%     301  271M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   405Gi    26Gi    95%    3.6M  271M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    26Gi    35%    427k  271M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    26Gi    35%    426k  271M    0%   /

```
✅ 主磁盘使用率: 35%

## OpenClaw 进程

✅ gateway: 运行中 (PIDs: 9441, 67803, 67809, 67810, 67811, 67813, 67814, 67815, 91541, 91568)
✅ agent: 运行中 (PIDs: 9441, 67803, 67809, 67810, 67811, 67813, 67814, 67815, 91541, 91568)
✅ browser: 运行中 (通过 ps 确认)

## 端口监听

✅ 端口 18789: 监听中
```
COMMAND   PID   USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
node    71611 3pigcn   18u  IPv4 0x2e8f81c88d4b6859      0t0  TCP localhost:18789 (LISTEN)
node    71611 3pigcn   19u  IPv6 0x9d7c5e5752f7fb62      0t0  TCP localhost:18789 (LISTEN)

```
✅ 端口 18800: 监听中
```
COMMAND     PID   USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
Google    67803 3pigcn   60u  IPv4 0xac55617238b236f9      0t0  TCP localhost:18800 (LISTEN)

```

## Gateway 健康检查

✅ Gateway health: {"ok":true,"status":"live"}
✅ Gateway status:
```
Service: LaunchAgent (loaded)
File logs: /tmp/openclaw/openclaw-2026-05-25.log
Command: /opt/homebrew/opt/node@22/bin/node /opt/homebrew/lib/node_modules/openclaw/dist/index.js gateway --port 18789
Service file: ~/Library/LaunchAgents/ai.openclaw.gateway.plist
Working dir: ~/.openclaw
Service env: OPENCLAW_GATEWAY_PORT=18789

Config (cli): ~/.openclaw/openclaw.json
Config (service): ~/.openclaw/openclaw.json

Gateway: bind=loopback (127.0.0.1), port=18789 (service args)
Probe target: ws://127.0.0.1:18789
Dashboard: http://127.0.0.1:18789/
Probe note: Loopback-only gateway; only local clients can connect.

CLI version: 2026.5.20 (/opt/homebrew/bin/openclaw)
Gateway version: 2026.5.20

Runtime: running (pid 71611)
Connectivity probe: ok
Capability: admin-capable

Listening: 127.0.0.1:18789
Troubles: run openclaw status
Troubleshooting: https://docs.openclaw.ai/troubleshooting

```

## Cron Jobs

✅ jobs.json: 存在 (16 个 job)
活跃任务: 10 个
- `每小时系统巡检`: {'kind': 'cron', 'expr': '0 * * * *', 'tz': 'Asia/Shanghai', 'staggerMs': 300000}
- `每日股票推荐`: {'kind': 'cron', 'expr': '0 20 * * *', 'tz': 'Asia/Shanghai'}
- `每日邮件摘要`: {'kind': 'cron', 'expr': '0 19 * * *', 'tz': 'Asia/Shanghai'}
- `每周主动提议`: {'kind': 'cron', 'expr': '0 18 * * 5', 'tz': 'Asia/Shanghai'}
- `Jira任务巡查`: {'kind': 'every', 'everyMs': 600000, 'anchorMs': 1776501898247}

## 最近 Cron Runs

最近 10 次运行记录:
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-25 09:57:02)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-25 09:34:02)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-25 09:04:30)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-25 08:50:20)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-25 08:03:21)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-24 20:10:47)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-24 19:02:59)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-24 18:03:28)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-24 15:03:50)
- `e2514301-9dc3-4ba8-9a9d-8a8fc9cc7ca0.jsonl` (更新时间: 2026-05-22 18:03:13)

## Gateway 日志异常

⚠️ `gateway.err.log` 中发现异常:
  - `Error: Failure while executing; `git clone https://github.com/pimalaya/homebrew-himalaya /opt/homebrew/Library/Taps/pima`
  - `2026-01-27T13:31:17.432Z [tools] exec failed: curl: (56) The requested URL returned error: 404`
  - `2026-01-27T13:31:22.005Z [tools] exec failed: curl: (56) The requested URL returned error: 404`
  - `fatal: repository 'https://github.com/pimalaya/homebrew-himalaya/' not found`
⚠️ `openclaw-2026-05-25.log` 中发现异常:
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
⚠️ `openclaw-2026-05-24.log` 中发现异常:
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`

## 系统整体状态

**Top 进程**:
```
Processes: 598 total, 6 running, 592 sleeping, 2847 threads 
2026/05/25 10:00:15
Load Avg: 3.10, 3.23, 3.11 
CPU usage: 20.86% user, 12.94% sys, 66.18% idle 
SharedLibs: 869M resident, 130M data, 202M linkedit.
MemRegions: 161430 total, 11G resident, 417M private, 7786M shared.
PhysMem: 31G used (8595M wired, 3102M compressor), 344M unused.
VM: 243T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 57967871/78G in, 46618951/54G out.
Disks: 67888669/876G read, 45427440/1923G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID STATE    BOOSTS   %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD   SYSMACH CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER            #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99930  IMTransferAgent  0.0  00:00.45 3   1   91     6736K 48K  1120K 99930 1    sleeping *10[1]   0.00000 0.00000    501 2476   210 1018    378     16384    3997    4092    1169    2     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
99060  ContainerMetadat 0.0  00:00.30 2   1   60     4208K 0B   2128K 99060 1    sleeping *0[6]    0.00000 0.00000    501 3169   159 1073    568     6876     1337    1211    4       0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
98518  com.apple.Safari 0.0  00:04.17 2   1   59     6593K 0B   4224K 98518 1    sleeping *0[1010] 0.00000 0.00000    501 26749  185 13371   9336    357765   110469  81211   67      296   0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95991  sirittsd         0.0  00:00.49 2   1   68     34M   0B   32M   95991 1    sleeping *0[3]    0.00000 0.00000    501 9001   216 346     190     8834     995     2367    2880    0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95945  com.apple.Mobile 0.0  06:34.91 4   1   115    56M   0B   49M   95945 1    sleeping *0[1]    0.00000 0.00000    0   201543 206 21978   10
```

## ⚠️ 异常项分析

### 1. `gateway.err.log` 中的异常（历史遗留，无需处理）
- **时间**: 2026-01-27（1月份，历史记录）
- **问题**: `pimalaya/homebrew-himalaya` 仓库不存在，curl 404
- **影响**: ⚪ 无影响 — 旧配置残留，不影响当前系统运行
- **建议**: 可安全忽略，或后续清理旧日志

### 2. `chrome-devtools` MCP Server 启动失败（需关注）
- **时间**: 2026-05-24 ~ 2026-05-25（近期持续发生）
- **问题**: `npx -y chrome-devtools-mcp@latest --slim --headless` 启动失败
- **错误类型**:
  - `MCP error -32000: Connection closed`（5月24日）
  - `MCP server connection timed out after 30000ms`（5月25日 09:35）
- **影响**: 🟡 低 — chrome-devtools MCP 是可选工具，不阻塞核心功能（gateway、agent、browser 均正常）
- **根因推测**:
  - npm 包下载/网络问题
  - npx 启动超时（30秒超时阈值）
- **建议**: 
  - 如不需要 Chrome DevTools MCP 功能，可忽略
  - 如需修复，可尝试：`npm install -g chrome-devtools-mcp@latest` 或检查网络连通性

### 3. 昨日（5/24）自巡检任务失败
- 日志显示：`cron: job run returned error status`
- 原因：脚本内搜索 chrome-devtools 日志的命令执行失败
- 今日巡检已成功执行，该问题已恢复

---

## 📋 结论与行动建议

| 检查项 | 状态 | 行动 |
|--------|------|------|
| macOS 资源 | ✅ 正常 | 无需行动 |
| 磁盘空间 | ✅ 正常 | 无需行动 |
| OpenClaw 进程 | ✅ 正常 | 无需行动 |
| 端口监听 | ✅ 正常 | 无需行动 |
| Gateway 健康 | ✅ 正常 | 无需行动 |
| Cron 任务 | ✅ 正常 | 无需行动 |
| chrome-devtools MCP | ⚠️ 启动失败 | **可选**：检查 npm/网络，或忽略 |
| 历史日志错误 | ⚠️ 旧记录 | 无需行动，可后续清理 |

**总体评估**: 系统核心功能全部正常，仅 chrome-devtools MCP Server 存在非致命性启动异常。建议根据是否需要该功能决定是否修复。

---
*报告更新 @ 2026-05-25 10:00:XX*
