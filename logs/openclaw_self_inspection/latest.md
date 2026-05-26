# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-27 06:32:31 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `6:32  up 9 days,  9:24, 6 users, load averages: 3.40 3.56 3.45`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                              253861.
Pages active:                            781442.
Pages inactive:                          753582.
Pages speculative:                        27205.
Pages throttled:                              0.
Pages wired down:                        139647.
Pages purgeable:                          27111.
"Translation faults":                7199927220.
Pages copy-on-write:                  195389977.
Pages zero filled:                   4793396160.
Pages reactivated:                     25239527.
Pages purged:                           2452988.
File-backed pages:                       390902.
Anonymous pages:                        1171327.
Pages stored in compressor:              287099.
Pages occupied by compressor:            106457.
Decompressions:                         7412639.
Compressions:                          17390334.
Pageins:                               62114232.
Pageouts:                               1916151.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 253826 
Pages purgeable: 27111 
Pages purged: 2452988 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 781460 
Pages inactive: 753582 
Pages speculative: 27210 
Pages throttled: 0 
Pages wired down: 139652 

Compressor Stats:
Pages used by compressor: 106457 
Pages decompressed: 7412639 
Pages compressed: 17390334 

File I/O:
Pageins: 62114233 
Pageouts: 1916151 

System-wide memory free percentage: 87%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    26Gi    35%    426k  270M    0%   /
devfs            201Ki   201Ki     0Bi   100%     694     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    26Gi     1%       0  270M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    26Gi    34%    1.8k  270M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    26Gi     3%     301  270M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   405Gi    26Gi    95%    3.7M  270M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    26Gi    35%    427k  270M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    26Gi    35%    426k  270M    0%   /

```
✅ 主磁盘使用率: 35%

## OpenClaw 进程

✅ gateway: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 71608, 71840, 73823, 88167)
✅ agent: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 71608, 71840, 73823, 88167)
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-27 06:32:22)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-27 06:01:20)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-27 06:00:45)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-27 04:54:27)
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
Processes: 646 total, 3 running, 643 sleeping, 2835 threads 
2026/05/27 06:32:34
Load Avg: 3.40, 3.56, 3.45 
CPU usage: 16.66% user, 11.80% sys, 71.52% idle 
SharedLibs: 889M resident, 133M data, 130M linkedit.
MemRegions: 166650 total, 5546M resident, 452M private, 1458M shared.
PhysMem: 27G used (2183M wired, 1663M compressor), 4368M unused.
VM: 263T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 77226096/89G in, 65651821/63G out.
Disks: 91828853/1487G read, 55761417/2595G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID STATE    BOOSTS   %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD   SYSMACH CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER            #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99060  ContainerMetadat 0.0  00:00.30 2   1   60     4208K 0B   3760K 99060 1    sleeping *0[6]    0.00000 0.00000    501 3233   159 1074    571     6878     1345    1223    4       0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
98518  com.apple.Safari 0.0  00:04.30 2   1   58     6609K 0B   5168K 98518 1    sleeping *0[1010] 0.00000 0.00000    501 29540  185 14809   10155   367251   114480  84359   93      296   0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95991  sirittsd         0.0  00:00.58 2   1   73     34M   0B   33M   95991 1    sleeping *0[4]    0.00000 0.00000    501 10580  216 415     237     9737     1236    3034    3027    0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95945  com.apple.Mobile 0.0  06:35.53 4   1   116    56M   0B   49M   95945 1    sleeping *0[1]    0.00000 0.00000    0   203759 206 23689   12022   20008977 29486   4487015 73303   507   0.0   0      0      0      root            N/A    N/A   N/A   N/A   N/A   N/A  
95939  softwareupdated  0.0  00:01.86 3   1   96     5152K 0B   2784K 95939 1    sleeping *0[26]   0.00000 0.00000    200 8420   170 30676 
```

---
*报告生成完成 @ 2026-05-27 06:32:31*
