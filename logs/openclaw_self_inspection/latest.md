# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-27 20:01:55 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `20:01  up 9 days, 22:54, 6 users, load averages: 3.33 3.13 2.98`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                               17236.
Pages active:                            898511.
Pages inactive:                          909233.
Pages speculative:                         4353.
Pages throttled:                              0.
Pages wired down:                        129562.
Pages purgeable:                          13761.
"Translation faults":                7587386573.
Pages copy-on-write:                  203055969.
Pages zero filled:                   5072118471.
Pages reactivated:                     29223659.
Pages purged:                           2685089.
File-backed pages:                       408088.
Anonymous pages:                        1404009.
Pages stored in compressor:              253869.
Pages occupied by compressor:            103220.
Decompressions:                         8005970.
Compressions:                          19255402.
Pageins:                               66141841.
Pageouts:                               2318605.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 17451 
Pages purgeable: 13761 
Pages purged: 2685089 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 898516 
Pages inactive: 909234 
Pages speculative: 4358 
Pages throttled: 0 
Pages wired down: 129563 

Compressor Stats:
Pages used by compressor: 103220 
Pages decompressed: 8005970 
Pages compressed: 19255402 

File I/O:
Pageins: 66141842 
Pageouts: 2318605 

System-wide memory free percentage: 88%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    24Gi    37%    426k  250M    0%   /
devfs            201Ki   201Ki     0Bi   100%     694     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    24Gi     1%       0  250M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    24Gi    36%    1.8k  250M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    24Gi     3%     301  250M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   407Gi    24Gi    95%    3.7M  250M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    24Gi    37%    427k  250M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    24Gi    37%    426k  250M    0%   /

```
✅ 主磁盘使用率: 37%

## OpenClaw 进程

✅ gateway: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 71608, 71840, 73823)
✅ agent: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 71608, 71840, 73823)
✅ browser: 运行中 (PIDs: 71840)

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
File logs: /tmp/openclaw/openclaw-2026-05-27.log
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-27 19:56:42)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-27 19:33:03)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-27 19:04:11)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-27 19:03:52)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-27 18:55:33)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-27 18:03:42)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-27 15:01:40)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-27 08:03:56)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-26 20:04:05)
- `e2514301-9dc3-4ba8-9a9d-8a8fc9cc7ca0.jsonl` (更新时间: 2026-05-22 18:03:13)

## Gateway 日志异常

⚠️ `openclaw-2026-05-27.log` 中发现异常:
  - `{"0":"{\"module\":\"cron\",\"storePath\":\"/Users/3pigcn/.openclaw/cron/jobs.json\"}","1":{"jobId":"8d0227c6-23ec-434c-8`
  - `{"0":"[tools] edit failed: Could not find the exact text in /Users/3pigcn/clawd/wing_recovery_alert.md. The old text mus`
  - `{"0":"[tools] edit failed: Could not find the exact text in /Users/3pigcn/clawd/wing_recovery_alert.md. The old text mus`
⚠️ `openclaw-2026-05-26.log` 中发现异常:
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"[tools] edit failed: Could not find the exact text in /Users/3pigcn/clawd/wing_recovery_alert.md. The old text mus`
  - `{"0":"[tools] edit failed: Could not find the exact text in /Users/3pigcn/clawd/wing_recovery_alert.md. The old text mus`

## 系统整体状态

**Top 进程**:
```
Processes: 480 total, 3 running, 477 sleeping, 2389 threads 
2026/05/27 20:01:57
Load Avg: 3.78, 3.23, 3.02 
CPU usage: 21.48% user, 13.22% sys, 65.28% idle 
SharedLibs: 925M resident, 112M data, 69M linkedit.
MemRegions: 152207 total, 5099M resident, 373M private, 1295M shared.
PhysMem: 31G used (2043M wired, 1613M compressor), 381M unused.
VM: 197T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 78783285/90G in, 67362139/63G out.
Disks: 99651914/1684G read, 58108648/2759G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG  CMPRS PGRP  PPID  STATE    BOOSTS  %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD  SYSMACH CSW    PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER   #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
88717  com.apple.appkit 0.0  00:02.78 4   2   297    34M   0B    26M   88717 1     sleeping  0[408] 0.00000 0.00000    501 20437  362 37125   17975   175310  85311   55314  117     87    0.0   0      0      0      3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
87380  zsh              0.0  00:00.04 1   0   22     4848K 0B    4512K 87380 87379 sleeping *0[1]   0.00000 0.00000    501 1883   394 89      37      21013   288     244    6       0     0.0   0      0      180    3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
87379  login            0.0  00:00.01 2   1   32     3120K 0B    2768K 87379 432   sleeping *0[9]   0.00000 0.00000    0   928    238 77      30      3757    263     154    2       0     0.0   0      0      180    root   N/A    N/A   N/A   N/A   N/A   N/A  
85430  IntelligencePlat 0.0  00:03.17 2   1   59     14M   1408K 14M   85430 1     sleeping  0[0]   0.00000 0.00000    501 8965   334 565     337     81968   21281   8934   416     1     0.0   0      0      0      3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
85186  audioanalyticsd  0.0  00:26.66 2   1   47     4128K 0B    1664K 85186 1     sleeping *0[23]  0.00000 0.00000    0   329272 170 1863    15993   1242884 20470   532636 1307    2931  0.0 
```

---
*报告生成完成 @ 2026-05-27 20:01:55*
