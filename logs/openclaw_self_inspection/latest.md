# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-25 13:30:34 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `13:30  up 7 days, 16:22, 6 users, load averages: 2.23 2.88 3.20`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                               90345.
Pages active:                            850554.
Pages inactive:                          831113.
Pages speculative:                        18670.
Pages throttled:                              0.
Pages wired down:                        132092.
Pages purgeable:                          13747.
"Translation faults":                5873897998.
Pages copy-on-write:                  165243539.
Pages zero filled:                   3881227951.
Pages reactivated:                     19215929.
Pages purged:                           2055335.
File-backed pages:                       617791.
Anonymous pages:                        1082546.
Pages stored in compressor:              352248.
Pages occupied by compressor:            139306.
Decompressions:                         6492606.
Compressions:                          14478441.
Pageins:                               45130363.
Pageouts:                               1096785.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 90309 
Pages purgeable: 13747 
Pages purged: 2055335 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 850553 
Pages inactive: 831122 
Pages speculative: 18676 
Pages throttled: 0 
Pages wired down: 132093 

Compressor Stats:
Pages used by compressor: 139306 
Pages decompressed: 6492606 
Pages compressed: 14478441 

File I/O:
Pageins: 45130364 
Pageouts: 1096785 

System-wide memory free percentage: 86%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    28Gi    33%    426k  289M    0%   /
devfs            201Ki   201Ki     0Bi   100%     694     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    28Gi     1%       0  289M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    28Gi    33%    1.8k  289M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    28Gi     3%     301  289M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   403Gi    28Gi    94%    3.6M  289M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    28Gi    33%    427k  289M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    28Gi    33%    426k  289M    0%   /

```
✅ 主磁盘使用率: 33%

## OpenClaw 进程

✅ gateway: 运行中 (PIDs: 36127, 46027, 67803, 67809, 67810, 67811, 67813, 67814, 67815, 91541)
✅ agent: 运行中 (PIDs: 36127, 46027, 67803, 67809, 67810, 67811, 67813, 67814, 67815, 91541)
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
Google    67803 3pigcn  107u  IPv4 0x8711b8571f9fbdf0      0t0  TCP localhost:18800->localhost:56193 (ESTABLISHED)
node      71611 3pigcn   26u  IPv4 0x97556a5cdf2dfa44      0t0  TCP localhost:56193->localhost:18800 (ESTABLISHED)

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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-25 13:27:02)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-25 13:01:27)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-25 13:00:37)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-25 12:52:24)
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
Processes: 589 total, 7 running, 582 sleeping, 2737 threads 
2026/05/25 13:30:37
Load Avg: 2.23, 2.88, 3.20 
CPU usage: 34.48% user, 17.93% sys, 47.58% idle 
SharedLibs: 879M resident, 104M data, 102M linkedit.
MemRegions: 162484 total, 6271M resident, 329M private, 1037M shared.
PhysMem: 30G used (2082M wired, 2177M compressor), 1688M unused.
VM: 239T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 66551506/85G in, 54317000/58G out.
Disks: 69046866/899G read, 46868376/1993G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID STATE    BOOSTS   %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD   SYSMACH CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER            #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99930  IMTransferAgent  0.0  00:01.03 3   1   92     6880K 48K  1392K 99930 1    sleeping *30[1]   0.00000 0.00000    501 4312   210 2491    1047    50883    11355   13204   1198    6     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
99060  ContainerMetadat 0.0  00:00.30 2   1   60     4208K 0B   3760K 99060 1    sleeping *0[6]    0.00000 0.00000    501 3169   159 1073    568     6876     1337    1211    4       0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
98518  com.apple.Safari 0.0  00:04.19 2   1   59     6593K 0B   4256K 98518 1    sleeping *0[1010] 0.00000 0.00000    501 27286  185 13523   9416    358797   110897  81588   73      296   0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95991  sirittsd         0.0  00:00.49 2   1   68     34M   0B   33M   95991 1    sleeping *0[3]    0.00000 0.00000    501 9001   216 346     190     8834     995     2367    2880    0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95945  com.apple.Mobile 0.0  06:34.96 4   1   115    56M   0B   49M   95945 1    sleeping *0[1]    0.00000 0.00000    0   202369 206 22131  
```

---
*报告生成完成 @ 2026-05-25 13:30:34*
