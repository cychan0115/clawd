# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-24 22:30:14 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `22:30  up 7 days,  1:22, 7 users, load averages: 3.12 3.28 3.12`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                              130912.
Pages active:                            823431.
Pages inactive:                          805511.
Pages speculative:                        21894.
Pages throttled:                              0.
Pages wired down:                        127718.
Pages purgeable:                          21054.
"Translation faults":                5220385534.
Pages copy-on-write:                  153451735.
Pages zero filled:                   3460069568.
Pages reactivated:                     14921192.
Pages purged:                           2022830.
File-backed pages:                       438304.
Anonymous pages:                        1212532.
Pages stored in compressor:              358209.
Pages occupied by compressor:            153447.
Decompressions:                         5343241.
Compressions:                          12544038.
Pageins:                               35398820.
Pageouts:                                847858.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 130619 
Pages purgeable: 21054 
Pages purged: 2022830 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 823439 
Pages inactive: 805512 
Pages speculative: 21899 
Pages throttled: 0 
Pages wired down: 127722 

Compressor Stats:
Pages used by compressor: 153447 
Pages decompressed: 5343241 
Pages compressed: 12544038 

File I/O:
Pageins: 35398821 
Pageouts: 847858 

System-wide memory free percentage: 86%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    27Gi    34%    426k  283M    0%   /
devfs            202Ki   202Ki     0Bi   100%     698     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    27Gi     1%       0  283M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    27Gi    33%    1.8k  283M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   690Mi    27Gi     3%     301  283M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   404Gi    27Gi    94%    3.7M  283M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    27Gi    34%    427k  283M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    27Gi    34%    426k  283M    0%   /

```
✅ 主磁盘使用率: 34%

## OpenClaw 进程

✅ gateway: 运行中 (PIDs: 11847, 11854, 11855, 11856, 35338, 50245)
✅ agent: 运行中 (PIDs: 11847, 11854, 11855, 11856, 35338, 50245)
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
Google    11847 3pigcn   50u  IPv4 0x89fc43d5333dc49c      0t0  TCP localhost:18800 (LISTEN)

```

## Gateway 健康检查

✅ Gateway health: {"ok":true,"status":"live"}
✅ Gateway status:
```
Service: LaunchAgent (loaded)
File logs: /tmp/openclaw/openclaw-2026-05-24.log
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-24 22:28:04)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-24 22:06:23)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-24 22:03:51)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-24 20:53:03)
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
⚠️ `openclaw-2026-05-24.log` 中发现异常:
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
⚠️ `openclaw-2026-05-23.log` 中发现异常:
  - `{"0":"[tools] web_search failed: SearXNG base URL is not configured. Set SEARXNG_BASE_URL or configure plugins.entries.s`
  - `{"0":"[tools] web_search failed: SearXNG base URL is not configured. Set SEARXNG_BASE_URL or configure plugins.entries.s`
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`

## 系统整体状态

**Top 进程**:
```
Processes: 609 total, 4 running, 605 sleeping, 2991 threads 
2026/05/24 22:30:17
Load Avg: 3.12, 3.28, 3.12 
CPU usage: 22.11% user, 14.57% sys, 63.31% idle 
SharedLibs: 858M resident, 129M data, 76M linkedit.
MemRegions: 272673 total, 6938M resident, 436M private, 1292M shared.
PhysMem: 29G used (2019M wired, 2398M compressor), 2314M unused.
VM: 258T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 56355281/78G in, 44815301/54G out.
Disks: 65194390/828G read, 42589383/1724G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG  CMPRS PGRP  PPID STATE    BOOSTS   %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD   SYSMACH CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER            #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99060  ContainerMetadat 0.0  00:00.30 2   1   60     4192K 0B    2048K 99060 1    sleeping *0[6]    0.00000 0.00000    501 3160   159 1072    565     6874     1329    1209    4       0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
98518  com.apple.Safari 0.0  00:04.15 2   1   58     6593K 0B    4080K 98518 1    sleeping *0[1010] 0.00000 0.00000    501 26101  185 13003   9121    355362   109438  80471   67      296   0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95991  sirittsd         0.0  00:00.44 2   1   68     34M   0B    33M   95991 1    sleeping *0[3]    0.00000 0.00000    501 8215   216 309     165     8368     857     1974    2809    0     0.0   0      0      0      3pigcn          N/A    N/A   N/A   N/A   N/A   N/A  
95945  com.apple.Mobile 0.0  06:34.68 4   1   115    58M   0B    52M   95945 1    sleeping *0[1]    0.00000 0.00000    0   201121 206 20555   10269   19971634 24366   4466897 73210   467   0.0   0      0      0      root            N/A    N/A   N/A   N/A   N/A   N/A  
95939  softwareupdated  0.0  00:01.04 3   1   85     5120K 0B    3920K 95939 1    sleeping *0[21]   0.00000 0.00000    200 5127   170 17
```

---
*报告生成完成 @ 2026-05-24 22:30:14*
