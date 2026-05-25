# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-25 19:30:13 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `19:30  up 7 days, 22:22, 8 users, load averages: 5.09 3.91 3.50`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                               50360.
Pages active:                            889469.
Pages inactive:                          884811.
Pages speculative:                         4108.
Pages throttled:                              0.
Pages wired down:                        139758.
Pages purgeable:                          30931.
"Translation faults":                6071498967.
Pages copy-on-write:                  169118663.
Pages zero filled:                   4024674127.
Pages reactivated:                     20108312.
Pages purged:                           2073765.
File-backed pages:                       474314.
Anonymous pages:                        1304074.
Pages stored in compressor:              264732.
Pages occupied by compressor:             94154.
Decompressions:                         6712090.
Compressions:                          14783468.
Pageins:                               47361364.
Pageouts:                               1175952.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 50321 
Pages purgeable: 30931 
Pages purged: 2073765 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 889474 
Pages inactive: 884812 
Pages speculative: 4111 
Pages throttled: 0 
Pages wired down: 139758 

Compressor Stats:
Pages used by compressor: 94154 
Pages decompressed: 6712090 
Pages compressed: 14783468 

File I/O:
Pageins: 47361366 
Pageouts: 1175952 

System-wide memory free percentage: 88%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    25Gi    36%    426k  262M    0%   /
devfs            202Ki   202Ki     0Bi   100%     698     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    25Gi     1%       0  262M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    25Gi    35%    1.8k  262M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    25Gi     3%     301  262M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   406Gi    25Gi    95%    3.7M  262M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    25Gi    36%    427k  262M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    25Gi    36%    426k  262M    0%   /

```
✅ 主磁盘使用率: 36%

## OpenClaw 进程

✅ gateway: 运行中 (PIDs: 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 81430)
✅ agent: 运行中 (PIDs: 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 81430)
✅ browser: 运行中 (通过 ps 确认)

## 端口监听

✅ 端口 18789: 监听中
```
COMMAND   PID   USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
node    53376 3pigcn   18u  IPv4 0x25209d3086dec88a      0t0  TCP localhost:18789 (LISTEN)
node    53376 3pigcn   19u  IPv6 0x3c5bb08b7043d9ac      0t0  TCP localhost:18789 (LISTEN)

```
✅ 端口 18800: 监听中
```
COMMAND     PID   USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
node      53376 3pigcn   36u  IPv4 0x408e2221d590a0d3      0t0  TCP localhost:55193->localhost:18800 (ESTABLISHED)
Google    54907 3pigcn   50u  IPv4 0xa226b67eccd21f3a      0t0  TCP localhost:18800 (LISTEN)
Google    54907 3pigcn  103u  IPv4 0xa14a99c8b00144fd      0t0  TCP localhost:18800->localhost:55193 (ESTABLISHED)

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

CLI version: 2026.5.22 (/opt/homebrew/bin/openclaw)
Gateway version: 2026.5.22

Runtime: running (pid 53376)
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-25 19:29:07)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-25 19:03:29)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-25 19:03:11)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-25 19:03:11)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-25 18:54:24)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-25 18:02:58)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-25 15:05:39)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-25 08:03:21)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-24 20:10:47)
- `e2514301-9dc3-4ba8-9a9d-8a8fc9cc7ca0.jsonl` (更新时间: 2026-05-22 18:03:13)

## Gateway 日志异常

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
Processes: 608 total, 4 running, 604 sleeping, 2845 threads 
2026/05/25 19:30:15
Load Avg: 5.09, 3.91, 3.50 
CPU usage: 27.40% user, 14.7% sys, 58.51% idle 
SharedLibs: 881M resident, 114M data, 80M linkedit.
MemRegions: 164969 total, 5393M resident, 456M private, 1608M shared.
PhysMem: 31G used (2201M wired, 1471M compressor), 825M unused.
VM: 248T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 68524062/86G in, 56313250/59G out.
Disks: 70616114/930G read, 48670561/2095G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID STATE    BOOSTS   %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD   SYSMACH CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER            #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99930  IMTransferAgent  0.0  00:01.80 3   1   92     6864K 48K  1344K 99930 1    sleeping *54[1]   0.00000 0.00000    501 5208   210 4453    1948    95236    20946   24927   1204    21    0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
99060  ContainerMetadat 0.0  00:00.30 2   1   60     4208K 0B   3760K 99060 1    sleeping *0[6]    0.00000 0.00000    501 3169   159 1073    568     6876     1337    1211    4       0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
98518  com.apple.Safari 0.0  00:04.21 2   1   59     6593K 0B   4192K 98518 1    sleeping *0[1010] 0.00000 0.00000    501 27457  185 13757   9538    360393   111525  82134   75      296   0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95991  sirittsd         0.0  00:00.49 2   1   68     34M   0B   32M   95991 1    sleeping *0[3]    0.00000 0.00000    501 9105   216 347     191     8842     1001    2374    2880    0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95945  com.apple.Mobile 0.0  06:35.04 4   1   115    56M   0B   49M   95945 1    sleeping *0[1]    0.00000 0.00000    0   202463 206 22364   11
```

---
*报告生成完成 @ 2026-05-25 19:30:13*
