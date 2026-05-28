# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-29 00:30:09 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `0:30  up 11 days,  3:22, 6 users, load averages: 1.99 1.87 1.79`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                              652276.
Pages active:                            585195.
Pages inactive:                          410479.
Pages speculative:                       183582.
Pages throttled:                              0.
Pages wired down:                        134298.
Pages purgeable:                          23079.
"Translation faults":                8304623196.
Pages copy-on-write:                  219702219.
Pages zero filled:                   5555632885.
Pages reactivated:                     38929686.
Pages purged:                           3232980.
File-backed pages:                       538942.
Anonymous pages:                         640314.
Pages stored in compressor:              227817.
Pages occupied by compressor:             96636.
Decompressions:                        12319037.
Compressions:                          27010022.
Pageins:                               76117151.
Pageouts:                               2996313.
Swapins:                                      7.
Swapouts:                                    16.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 652235 
Pages purgeable: 23079 
Pages purged: 3232980 

Swap I/O:
Swapins: 7 
Swapouts: 16 

Page Q counts:
Pages active: 585196 
Pages inactive: 410479 
Pages speculative: 183582 
Pages throttled: 0 
Pages wired down: 134298 

Compressor Stats:
Pages used by compressor: 96636 
Pages decompressed: 12319037 
Pages compressed: 27010022 

File I/O:
Pageins: 76117152 
Pageouts: 2996313 

System-wide memory free percentage: 88%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    34Gi    29%    426k  355M    0%   /
devfs            201Ki   201Ki     0Bi   100%     694     0  100%   /dev
/dev/disk3s6     460Gi   1.0Gi    34Gi     3%       1  355M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    34Gi    29%    1.8k  355M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    34Gi     2%     301  355M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   396Gi    34Gi    93%    3.7M  355M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    34Gi    29%    427k  355M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    34Gi    29%    426k  355M    0%   /

```
✅ 主磁盘使用率: 29%

## OpenClaw 进程

✅ gateway: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 71324, 71608, 71840, 73823)
✅ agent: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 71324, 71608, 71840, 73823)
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-29 00:24:17)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-29 00:01:40)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-29 00:01:20)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-28 22:58:24)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-28 20:11:22)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-28 19:03:16)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-28 18:05:35)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-28 15:03:55)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-28 08:03:55)
- `e2514301-9dc3-4ba8-9a9d-8a8fc9cc7ca0.jsonl` (更新时间: 2026-05-22 18:03:13)

## Gateway 日志异常

⚠️ `openclaw-2026-05-29.log` 中发现异常:
  - `{"0":"[tools] edit failed: Found 3 occurrences of the text in /Users/3pigcn/clawd/wing_recovery_alert.md. The text must `
  - `{"0":"[tools] edit failed: Found 3 occurrences of the text in /Users/3pigcn/clawd/wing_recovery_alert.md. The text must `
  - `{"0":"[tools] edit failed: Found 3 occurrences of the text in /Users/3pigcn/clawd/wing_recovery_alert.md. The text must `
⚠️ `openclaw-2026-05-28.log` 中发现异常:
  - `{"0":"{\"module\":\"cron\",\"storePath\":\"/Users/3pigcn/.openclaw/cron/jobs.json\"}","1":{"jobId":"8d0227c6-23ec-434c-8`
  - `{"0":"[tools] edit failed: Found 7 occurrences of the text in /Users/3pigcn/clawd/wing_recovery_alert.md. The text must `
  - `{"0":"[tools] edit failed: Found 7 occurrences of the text in /Users/3pigcn/clawd/wing_recovery_alert.md. The text must `

## 系统整体状态

**Top 进程**:
```
Processes: 561 total, 3 running, 558 sleeping, 2465 threads 
2026/05/29 00:30:10
Load Avg: 1.99, 1.87, 1.79 
CPU usage: 4.31% user, 18.96% sys, 76.72% idle 
SharedLibs: 967M resident, 151M data, 136M linkedit.
MemRegions: 157455 total, 6183M resident, 630M private, 1452M shared.
PhysMem: 19G used (2105M wired, 1510M compressor), 13G unused.
VM: 229T vsize, 5703M framework vsize, 7(0) swapins, 16(0) swapouts.
Networks: packets: 85592703/101G in, 74575433/74G out.
Disks: 115837700/2106G read, 63415026/3105G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID STATE    BOOSTS  %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD SYSMACH CSW  PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER            #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99571  helpd            0.0  00:01.42 4   2   78     11M   448K 0B    99571 1    sleeping *0[1]   0.00000 0.00000    501 3100   196 628     175     32011  2878    4395 171     73    0.0   0      0      40     3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
99445  com.apple.access 0.0  00:00.04 2   1   36     1904K 0B   0B    99445 1    sleeping *0[5]   0.00000 0.00000    501 843    119 124     44      633    286     200  2       1     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
99442  com.apple.hiserv 0.0  00:00.02 2   1   47     1952K 0B   0B    99442 1    sleeping *0[5]   0.00000 0.00000    501 703    122 160     54      570    347     71   2       2     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
99441  nsattributedstri 0.0  00:00.50 5   2   262    9649K 0B   0B    99441 1    sleeping *148[4] 0.00000 0.00000    501 6134   318 4943    3427    21865  14113   4257 4       138   0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
99439  com.apple.access 0.0  00:00.04 2   1   36     1968K 0B   0B    99439 1    sleeping *0[2]   0.00000 0.00000    200 844    119 120     40      606    278     142  2
```

---
*报告生成完成 @ 2026-05-29 00:30:09*
