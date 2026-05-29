# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-29 21:30:08 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `21:30  up 13:46, 5 users, load averages: 1.78 1.98 2.13`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                               49627.
Pages active:                            884107.
Pages inactive:                          862794.
Pages speculative:                        20485.
Pages throttled:                              0.
Pages wired down:                        144948.
Pages purgeable:                          78145.
"Translation faults":                 315330106.
Pages copy-on-write:                   17691940.
Pages zero filled:                    168283989.
Pages reactivated:                      1626384.
Pages purged:                            449125.
File-backed pages:                       836513.
Anonymous pages:                         930873.
Pages stored in compressor:              236299.
Pages occupied by compressor:            100179.
Decompressions:                          294127.
Compressions:                            845300.
Pageins:                                8602956.
Pageouts:                                 53057.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 49602 
Pages purgeable: 78145 
Pages purged: 449125 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 884176 
Pages inactive: 862794 
Pages speculative: 20488 
Pages throttled: 0 
Pages wired down: 144949 

Compressor Stats:
Pages used by compressor: 100179 
Pages decompressed: 294127 
Pages compressed: 845300 

File I/O:
Pageins: 8602958 
Pageouts: 53057 

System-wide memory free percentage: 88%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    17Gi    35Gi    33%    427k  368M    0%   /
devfs            200Ki   200Ki     0Bi   100%     691     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    35Gi     1%       0  368M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    15Gi    35Gi    30%    2.0k  368M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   349Mi    35Gi     1%     176  368M    0%   /System/Volumes/Update
/dev/disk2s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk2s1     500Mi   6.0Mi   483Mi     2%      31  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk2s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   391Gi    35Gi    92%    3.7M  368M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk1s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    17Gi    35Gi    33%    459k  368M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    17Gi    35Gi    33%    427k  368M    0%   /

```
✅ 主磁盘使用率: 33%

## OpenClaw 进程

✅ gateway: 运行中 (通过 ps 确认)
✅ agent: 活跃 (sessions.json 更新于 0 分钟前)
✅ browser: 未运行（按需启动，非异常）

## 端口监听

✅ 端口 18789 (gateway): 监听中
```
COMMAND  PID   USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
node    3824 3pigcn   18u  IPv4 0x3c2dfd9395a938c0      0t0  TCP localhost:18789 (LISTEN)
node    3824 3pigcn   19u  IPv6 0xdfa5512ac805e668      0t0  TCP localhost:18789 (LISTEN)

```
✅ 端口 18800 (browser CDP): 未监听（browser 按需启动，非异常）

## Gateway 健康检查

✅ Gateway health: {"ok":true,"status":"live"}
✅ Gateway status:
```
Service: LaunchAgent (loaded)
File logs: /tmp/openclaw/openclaw-2026-05-29.log
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

CLI version: 2026.5.27 (/opt/homebrew/bin/openclaw)
Gateway version: 2026.5.27

Runtime: running (pid 3824)
Connectivity probe: ok
Capability: admin-capable

Listening: 127.0.0.1:18789, [::1]:18789
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-29 21:25:00)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-29 21:01:37)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-29 21:01:05)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-29 21:00:28)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-29 20:00:29)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-29 19:04:06)
- `e2514301-9dc3-4ba8-9a9d-8a8fc9cc7ca0.jsonl` (更新时间: 2026-05-29 18:02:33)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-29 18:02:33)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-29 15:01:12)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-29 08:06:41)

## Gateway 日志异常

✅ 最近日志中未检测到明显异常

## 系统整体状态

**Top 进程**:
```
Processes: 819 total, 2 running, 817 sleeping, 4083 threads 
2026/05/29 21:30:10
Load Avg: 1.72, 1.96, 2.12 
CPU usage: 8.48% user, 14.13% sys, 77.38% idle 
SharedLibs: 1118M resident, 171M data, 345M linkedit.
MemRegions: 443977 total, 8165M resident, 795M private, 5101M shared.
PhysMem: 30G used (2436M wired, 1565M compressor), 1100M unused.
VM: 353T vsize, 5702M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 14273768/34G in, 6724070/23G out.
Disks: 9630793/217G read, 4813277/234G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG  CMPRS PGRP  PPID  STATE    BOOSTS  %CPU_ME %CPU_OTHRS UID FAULTS COW  MSGSENT MSGRECV SYSBSD SYSMACH CSW    PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER   #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99877  top              0.0  00:00.28 1/1 0   16     5824K 0B    0B    3824  99783 running  *0[1]   0.00000 0.00000    0   1457   106  937156  468577  4276   475186  52     2       0     0.0   0      0      180    root   N/A    N/A   N/A   N/A   N/A   N/A  
99814  sleep            0.0  00:00.00 1   0   11     976K  0B    0B    1439  1439  sleeping *0[1]   0.00000 0.00000    501 249    55   26      13      127    69      2      1       0     0.0   0      0      180    3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
99783  Python           0.0  00:00.56 1   0   15     11M   0B    0B    3824  3824  sleeping *0[1]   0.00000 0.00000    501 5045   1155 105     42      2014   378     146    46      0     0.0   0      0      180    3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
99782  curl             0.0  00:00.01 3   2   34     2992K 0B    0B    1456  1456  sleeping *0[1]   0.00000 0.00000    501 572    107  72      20      402    163     46     2       0     0.0   0      0      180    3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
99724  ssh              0.0  00:00.13 1   0   22     4208K 0B    0B    1456  1456  sleeping *0[1]   0.00000 0.00000    501 580    95   51      17      527    122     45     1       0     0.0   0
```

---
*报告生成完成 @ 2026-05-29 21:30:08*
