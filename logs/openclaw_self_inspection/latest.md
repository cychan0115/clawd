# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-27 03:33:43 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `3:33  up 9 days,  6:26, 6 users, load averages: 3.23 2.87 2.88`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                                6374.
Pages active:                            905539.
Pages inactive:                          902368.
Pages speculative:                         3456.
Pages throttled:                              0.
Pages wired down:                        143935.
Pages purgeable:                          30897.
"Translation faults":                7113980737.
Pages copy-on-write:                  193932202.
Pages zero filled:                   4732585071.
Pages reactivated:                     24875197.
Pages purged:                           2422715.
File-backed pages:                       406281.
Anonymous pages:                        1405082.
Pages stored in compressor:              270809.
Pages occupied by compressor:            100325.
Decompressions:                         7350809.
Compressions:                          17306767.
Pageins:                               60396693.
Pageouts:                               1846766.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 6597 
Pages purgeable: 30897 
Pages purged: 2422715 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 905546 
Pages inactive: 902369 
Pages speculative: 3462 
Pages throttled: 0 
Pages wired down: 143935 

Compressor Stats:
Pages used by compressor: 100325 
Pages decompressed: 7350809 
Pages compressed: 17306767 

File I/O:
Pageins: 60396694 
Pageouts: 1846766 

System-wide memory free percentage: 88%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    25Gi    36%    426k  263M    0%   /
devfs            201Ki   201Ki     0Bi   100%     694     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    25Gi     1%       0  263M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    25Gi    35%    1.8k  263M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    25Gi     3%     301  263M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   406Gi    25Gi    95%    3.7M  263M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    25Gi    36%    427k  263M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    25Gi    36%    426k  263M    0%   /

```
✅ 主磁盘使用率: 36%

## OpenClaw 进程

✅ gateway: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 71608, 71840, 73823, 76045)
✅ agent: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 71608, 71840, 73823, 76045)
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-27 03:33:30)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-27 03:04:06)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-27 03:03:54)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-27 02:54:30)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-26 20:04:05)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-26 19:03:02)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-26 18:08:26)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-26 15:01:26)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-26 08:07:37)
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
Processes: 651 total, 4 running, 647 sleeping, 2883 threads 
2026/05/27 03:33:46
Load Avg: 3.21, 2.87, 2.88 
CPU usage: 25.87% user, 16.8% sys, 58.4% idle 
SharedLibs: 908M resident, 141M data, 133M linkedit.
MemRegions: 166654 total, 5780M resident, 526M private, 1491M shared.
PhysMem: 31G used (2246M wired, 1568M compressor), 360M unused.
VM: 265T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 77007566/89G in, 65399203/62G out.
Disks: 89758519/1431G read, 55112702/2547G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID STATE    BOOSTS   %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD   SYSMACH CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER            #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99060  ContainerMetadat 0.0  00:00.30 2   1   60     4208K 0B   3760K 99060 1    sleeping *0[6]    0.00000 0.00000    501 3233   159 1074    571     6878     1345    1223    4       0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
98518  com.apple.Safari 0.0  00:04.29 2   1   58     6561K 0B   3760K 98518 1    sleeping *0[1010] 0.00000 0.00000    501 29138  185 14715   10098   366652   114212  84148   93      296   0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95991  sirittsd         0.0  00:00.54 2   1   69     34M   0B   32M   95991 1    sleeping *0[3]    0.00000 0.00000    501 10076  216 386     219     9332     1149    2719    2961    0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95945  com.apple.Mobile 0.0  06:35.48 4   1   115    56M   0B   49M   95945 1    sleeping *0[1]    0.00000 0.00000    0   203714 206 23556   11935   20006918 29243   4485935 73303   505   0.0   0      0      0      root            N/A    N/A   N/A   N/A   N/A   N/A  
95939  softwareupdated  0.0  00:01.82 3   1   91     5136K 0B   2224K 95939 1    sleeping *0[26]   0.00000 0.00000    200 7959   170 30627   1
```

---
*报告生成完成 @ 2026-05-27 03:33:43*
