# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-26 11:30:11 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `11:30  up 8 days, 14:22, 7 users, load averages: 3.03 3.13 3.31`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                                4076.
Pages active:                            903748.
Pages inactive:                          902371.
Pages speculative:                          647.
Pages throttled:                              0.
Pages wired down:                        139556.
Pages purgeable:                          19409.
"Translation faults":                6611685456.
Pages copy-on-write:                  181099007.
Pages zero filled:                   4394298214.
Pages reactivated:                     23084041.
Pages purged:                           2253632.
File-backed pages:                       637617.
Anonymous pages:                        1169149.
Pages stored in compressor:              300402.
Pages occupied by compressor:            111914.
Decompressions:                         7181431.
Compressions:                          16510020.
Pageins:                               53646007.
Pageouts:                               1408936.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 4065 
Pages purgeable: 19404 
Pages purged: 2253632 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 903741 
Pages inactive: 902379 
Pages speculative: 650 
Pages throttled: 0 
Pages wired down: 139556 

Compressor Stats:
Pages used by compressor: 111914 
Pages decompressed: 7181431 
Pages compressed: 16510020 

File I/O:
Pageins: 53646009 
Pageouts: 1408936 

System-wide memory free percentage: 87%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    26Gi    35%    426k  269M    0%   /
devfs            201Ki   201Ki     0Bi   100%     696     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    26Gi     1%       0  269M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    26Gi    34%    1.8k  269M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    26Gi     3%     301  269M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   405Gi    26Gi    95%    3.7M  269M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    26Gi    35%    427k  269M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    26Gi    35%    426k  269M    0%   /

```
✅ 主磁盘使用率: 35%

## OpenClaw 进程

✅ gateway: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656)
✅ agent: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656)
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
File logs: /tmp/openclaw/openclaw-2026-05-26.log
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-26 11:29:49)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-26 11:05:16)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-26 11:05:00)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-26 10:56:04)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-26 08:07:37)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-25 20:02:32)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-25 19:03:11)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-25 18:02:58)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-25 15:05:39)
- `e2514301-9dc3-4ba8-9a9d-8a8fc9cc7ca0.jsonl` (更新时间: 2026-05-22 18:03:13)

## Gateway 日志异常

⚠️ `openclaw-2026-05-26.log` 中发现异常:
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"[tools] edit failed: Could not find the exact text in /Users/3pigcn/clawd/wing_recovery_alert.md. The old text mus`
  - `{"0":"[tools] edit failed: Could not find the exact text in /Users/3pigcn/clawd/wing_recovery_alert.md. The old text mus`
⚠️ `openclaw-2026-05-25.log` 中发现异常:
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`

## 系统整体状态

**Top 进程**:
```
Processes: 628 total, 6 running, 622 sleeping, 2819 threads 
2026/05/26 11:30:14
Load Avg: 3.03, 3.13, 3.31 
CPU usage: 28.47% user, 15.97% sys, 55.55% idle 
SharedLibs: 903M resident, 129M data, 79M linkedit.
MemRegions: 164596 total, 5126M resident, 457M private, 1360M shared.
PhysMem: 31G used (2180M wired, 1749M compressor), 358M unused.
VM: 256T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 72990198/88G in, 61115968/61G out.
Disks: 79965006/1173G read, 52011294/2332G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID STATE    BOOSTS   %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD   SYSMACH CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER            #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99060  ContainerMetadat 0.0  00:00.30 2   1   60     4208K 0B   3760K 99060 1    sleeping *0[6]    0.00000 0.00000    501 3233   159 1074    571     6878     1345    1223    4       0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
98518  com.apple.Safari 0.0  00:04.26 2   1   58     6577K 0B   4208K 98518 1    sleeping *0[1010] 0.00000 0.00000    501 28562  185 14236   9818    363523   112875  83162   93      296   0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95991  sirittsd         0.0  00:00.53 2   1   68     34M   0B   32M   95991 1    sleeping *0[3]    0.00000 0.00000    501 9905   216 373     208     9244     1087    2644    2955    0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95945  com.apple.Mobile 0.0  06:35.26 4   1   115    56M   0B   49M   95945 1    sleeping *0[1]    0.00000 0.00000    0   203472 206 22894   11559   19996350 27984   4480093 73300   497   0.0   0      0      0      root            N/A    N/A   N/A   N/A   N/A   N/A  
95939  softwareupdated  0.0  00:01.53 3   1   91     5136K 0B   2752K 95939 1    sleeping *0[26]   0.00000 0.00000    200 7381   170 24230   
```

---
*报告生成完成 @ 2026-05-26 11:30:11*
