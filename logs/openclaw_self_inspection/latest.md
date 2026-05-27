# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-28 04:30:42 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `4:30  up 10 days,  7:23, 6 users, load averages: 2.80 3.64 3.49`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                              336762.
Pages active:                            747243.
Pages inactive:                          727456.
Pages speculative:                        21073.
Pages throttled:                              0.
Pages wired down:                        135441.
Pages purgeable:                          24898.
"Translation faults":                7825964409.
Pages copy-on-write:                  206943746.
Pages zero filled:                   5233619865.
Pages reactivated:                     30215139.
Pages purged:                           2797080.
File-backed pages:                       389786.
Anonymous pages:                        1105986.
Pages stored in compressor:              238644.
Pages occupied by compressor:             94705.
Decompressions:                         8090420.
Compressions:                          19361603.
Pageins:                               69095911.
Pageouts:                               2530788.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 336471 
Pages purgeable: 24898 
Pages purged: 2797080 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 747256 
Pages inactive: 727457 
Pages speculative: 21078 
Pages throttled: 0 
Pages wired down: 135445 

Compressor Stats:
Pages used by compressor: 94705 
Pages decompressed: 8090420 
Pages compressed: 19361603 

File I/O:
Pageins: 69095912 
Pageouts: 2530788 

System-wide memory free percentage: 88%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    26Gi    35%    426k  268M    0%   /
devfs            201Ki   201Ki     0Bi   100%     694     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    26Gi     1%       0  268M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    26Gi    35%    1.8k  268M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    26Gi     3%     301  268M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   405Gi    26Gi    95%    3.7M  268M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    26Gi    35%    427k  268M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    26Gi    35%    426k  268M    0%   /

```
✅ 主磁盘使用率: 35%

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
File logs: /tmp/openclaw/openclaw-2026-05-28.log
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-28 04:26:22)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-28 04:01:19)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-28 04:00:45)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-28 02:54:40)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-27 20:03:47)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-27 19:03:52)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-27 18:03:42)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-27 15:01:40)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-27 08:03:56)
- `e2514301-9dc3-4ba8-9a9d-8a8fc9cc7ca0.jsonl` (更新时间: 2026-05-22 18:03:13)

## Gateway 日志异常

⚠️ `openclaw-2026-05-28.log` 中发现异常:
  - `{"0":"{\"module\":\"cron\",\"storePath\":\"/Users/3pigcn/.openclaw/cron/jobs.json\"}","1":{"jobId":"8d0227c6-23ec-434c-8`
  - `{"0":"[tools] edit failed: Found 7 occurrences of the text in /Users/3pigcn/clawd/wing_recovery_alert.md. The text must `
  - `{"0":"[tools] edit failed: Found 7 occurrences of the text in /Users/3pigcn/clawd/wing_recovery_alert.md. The text must `
⚠️ `openclaw-2026-05-27.log` 中发现异常:
  - `{"0":"{\"module\":\"cron\",\"storePath\":\"/Users/3pigcn/.openclaw/cron/jobs.json\"}","1":{"jobId":"8d0227c6-23ec-434c-8`
  - `{"0":"[tools] edit failed: Could not find the exact text in /Users/3pigcn/clawd/wing_recovery_alert.md. The old text mus`
  - `{"0":"[tools] edit failed: Could not find the exact text in /Users/3pigcn/clawd/wing_recovery_alert.md. The old text mus`

## 系统整体状态

**Top 进程**:
```
Processes: 566 total, 4 running, 562 sleeping, 2528 threads 
2026/05/28 04:30:45
Load Avg: 3.22, 3.71, 3.52 
CPU usage: 21.53% user, 13.7% sys, 65.38% idle 
SharedLibs: 926M resident, 137M data, 86M linkedit.
MemRegions: 158057 total, 5909M resident, 481M private, 1447M shared.
PhysMem: 26G used (2120M wired, 1480M compressor), 5535M unused.
VM: 231T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 79857603/91G in, 68478389/64G out.
Disks: 104233984/1805G read, 59866528/2888G written.

PID    COMMAND   %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID  STATE    BOOSTS %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD SYSMACH CSW PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER               #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
91040  top       0.0  00:00.13 1/1 0   16     3920K 0B   0B    53376 90982 running  *0[1]  0.00000 0.00000    0   1100   114 350562  175280  3011   179568  8   7       0     0.0   0      0      180    root               N/A    N/A   N/A   N/A   N/A   N/A  
90982  Python    0.0  00:01.51 1   0   15     12M   0B   0B    53376 53376 sleeping *0[1]  0.00000 0.00000    501 4518   997 99      39      1919   406     120 63      0     0.0   0      0      180    3pigcn             N/A    N/A   N/A   N/A   N/A   N/A  
90977  sleep     0.0  00:00.00 1   0   11     976K  0B   0B    607   607   sleeping *0[1]  0.00000 0.00000    501 247    58  26      13      127    67      2   1       0     0.0   0      0      180    3pigcn             N/A    N/A   N/A   N/A   N/A   N/A  
90975  ssh       0.0  00:00.11 1   0   22     3392K 0B   0B    607   607   sleeping *0[1]  0.00000 0.00000    501 538    102 51      17      524    117     31  1       0     0.0   0      0      180    3pigcn             N/A    N/A   N/A   N/A   N/A   N/A  
90961  sleep     0.0  00:00.00 1   0   11     960K  0B   0B    588   588   sleeping *0[1]  0.00000 0.00000    501 249    55  26      13      127    69      2   1       0     0.0   0      0      1
```

---
*报告生成完成 @ 2026-05-28 04:30:42*
