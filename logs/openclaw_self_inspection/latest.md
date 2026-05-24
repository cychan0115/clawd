# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-25 05:31:31 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `5:31  up 7 days,  8:23, 6 users, load averages: 3.26 3.45 3.34`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                              100509.
Pages active:                            866821.
Pages inactive:                          840387.
Pages speculative:                        25780.
Pages throttled:                              0.
Pages wired down:                        129937.
Pages purgeable:                          26929.
"Translation faults":                5460478806.
Pages copy-on-write:                  157953934.
Pages zero filled:                   3633376179.
Pages reactivated:                     16144054.
Pages purged:                           2030945.
File-backed pages:                       449963.
Anonymous pages:                        1283025.
Pages stored in compressor:              256953.
Pages occupied by compressor:             99309.
Decompressions:                         5433287.
Compressions:                          12591644.
Pageins:                               38478231.
Pageouts:                                901007.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 100732 
Pages purgeable: 26945 
Pages purged: 2030945 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 866823 
Pages inactive: 840393 
Pages speculative: 25783 
Pages throttled: 0 
Pages wired down: 129939 

Compressor Stats:
Pages used by compressor: 99309 
Pages decompressed: 5433287 
Pages compressed: 12591644 

File I/O:
Pageins: 38478233 
Pageouts: 901007 

System-wide memory free percentage: 88%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    28Gi    33%    426k  292M    0%   /
devfs            200Ki   200Ki     0Bi   100%     692     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    28Gi     1%       0  292M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    28Gi    33%    1.8k  292M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    28Gi     3%     301  292M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   403Gi    28Gi    94%    3.6M  292M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    28Gi    33%    427k  292M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    28Gi    33%    426k  292M    0%   /

```
✅ 主磁盘使用率: 33%

## OpenClaw 进程

✅ gateway: 运行中 (PIDs: 67803, 67809, 67810, 67811, 67813, 67814, 67815, 87889)
✅ agent: 运行中 (PIDs: 67803, 67809, 67810, 67811, 67813, 67814, 67815, 87889)
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-25 05:27:23)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-25 05:03:00)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-25 05:02:43)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-25 04:50:27)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-24 20:10:47)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-24 19:02:59)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-24 18:03:28)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-24 15:03:50)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-24 08:05:30)
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
Processes: 582 total, 3 running, 579 sleeping, 2680 threads 
2026/05/25 05:31:33
Load Avg: 3.16, 3.43, 3.33 
CPU usage: 11.81% user, 10.23% sys, 77.95% idle 
SharedLibs: 874M resident, 129M data, 201M linkedit.
MemRegions: 143644 total, 6482M resident, 512M private, 1413M shared.
PhysMem: 30G used (2032M wired, 1552M compressor), 1968M unused.
VM: 235T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 56807975/78G in, 45363148/54G out.
Disks: 66812733/853G read, 44498054/1868G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID STATE    BOOSTS   %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD   SYSMACH CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER            #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99060  ContainerMetadat 0.0  00:00.30 2   1   60     4208K 0B   2032K 99060 1    sleeping *0[6]    0.00000 0.00000    501 3169   159 1073    568     6876     1337    1211    4       0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
98518  com.apple.Safari 0.0  00:04.16 2   1   58     6625K 0B   5088K 98518 1    sleeping *0[1010] 0.00000 0.00000    501 26361  185 13211   9248    356702   110025  80884   67      296   0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95991  sirittsd         0.0  00:00.48 2   1   71     34M   0B   29M   95991 1    sleeping *0[3]    0.00000 0.00000    501 8881   216 343     187     8811     975     2352    2880    0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95945  com.apple.Mobile 0.0  06:34.85 4   1   115    56M   0B   48M   95945 1    sleeping *0[1]    0.00000 0.00000    0   201485 206 21824   10890   19976762 25822   4469500 73232   472   0.0   0      0      0      root            N/A    N/A   N/A   N/A   N/A   N/A  
95939  softwareupdated  0.0  00:01.11 3   1   84     5120K 0B   2960K 95939 1    sleeping *0[25]   0.00000 0.00000    200 5497   170 17722  
```

---
*报告生成完成 @ 2026-05-25 05:31:31*
