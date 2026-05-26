# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-26 23:00:09 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `23:00  up 9 days,  1:52, 8 users, load averages: 4.14 4.09 4.36`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                                4432.
Pages active:                            908921.
Pages inactive:                          907328.
Pages speculative:                          929.
Pages throttled:                              0.
Pages wired down:                        137194.
Pages purgeable:                          29261.
"Translation faults":                6962936001.
Pages copy-on-write:                  190966135.
Pages zero filled:                   4636629719.
Pages reactivated:                     24473856.
Pages purged:                           2386682.
File-backed pages:                       399084.
Anonymous pages:                        1418094.
Pages stored in compressor:              274071.
Pages occupied by compressor:            104021.
Decompressions:                         7331893.
Compressions:                          17253590.
Pageins:                               58862894.
Pageouts:                               1729200.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 4171 
Pages purgeable: 29261 
Pages purged: 2386682 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 908924 
Pages inactive: 907328 
Pages speculative: 941 
Pages throttled: 0 
Pages wired down: 137195 

Compressor Stats:
Pages used by compressor: 104021 
Pages decompressed: 7331893 
Pages compressed: 17253590 

File I/O:
Pageins: 58862896 
Pageouts: 1729200 

System-wide memory free percentage: 88%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    25Gi    36%    426k  258M    0%   /
devfs            202Ki   202Ki     0Bi   100%     698     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    25Gi     1%       0  258M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    25Gi    35%    1.8k  258M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    25Gi     3%     301  258M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   406Gi    25Gi    95%    3.7M  258M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    25Gi    36%    427k  258M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    25Gi    36%    426k  258M    0%   /

```
✅ 主磁盘使用率: 36%

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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-26 22:59:38)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-26 22:54:31)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-26 22:30:37)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-26 22:01:21)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-26 20:04:05)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-26 19:03:02)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-26 18:08:26)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-26 15:01:26)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-26 08:07:37)
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
Processes: 634 total, 5 running, 629 sleeping, 2813 threads 
2026/05/26 23:00:11
Load Avg: 4.21, 4.10, 4.36 
CPU usage: 23.23% user, 9.85% sys, 66.90% idle 
SharedLibs: 906M resident, 141M data, 130M linkedit.
MemRegions: 166374 total, 5683M resident, 517M private, 1530M shared.
PhysMem: 31G used (2144M wired, 1625M compressor), 352M unused.
VM: 258T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 74982299/89G in, 63371975/62G out.
Disks: 86440533/1359G read, 54247341/2493G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID STATE    BOOSTS   %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD   SYSMACH CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER            #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99060  ContainerMetadat 0.0  00:00.30 2   1   60     4208K 0B   3760K 99060 1    sleeping *0[6]    0.00000 0.00000    501 3233   159 1074    571     6878     1345    1223    4       0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
98518  com.apple.Safari 0.0  00:04.28 2   1   59     6609K 0B   3808K 98518 1    sleeping *0[1010] 0.00000 0.00000    501 29043  185 14563   10011   365651   113792  83844   93      296   0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95991  sirittsd         0.0  00:00.53 2   1   68     34M   0B   32M   95991 1    sleeping *0[3]    0.00000 0.00000    501 9953   216 377     212     9277     1107    2674    2955    0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95945  com.apple.Mobile 0.0  06:35.42 4   1   115    56M   0B   49M   95945 1    sleeping *0[1]    0.00000 0.00000    0   203654 206 23423   11836   20003870 28955   4484264 73303   503   0.0   0      0      0      root            N/A    N/A   N/A   N/A   N/A   N/A  
95939  softwareupdated  0.0  00:01.78 3   1   91     5120K 0B   2240K 95939 1    sleeping *0[26]   0.00000 0.00000    200 7801   170 30578   
```

---
*报告生成完成 @ 2026-05-26 23:00:09*
