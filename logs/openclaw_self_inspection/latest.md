# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-29 13:30:05 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `13:30  up  5:46, 6 users, load averages: 2.66 2.65 2.65`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                                9048.
Pages active:                            858441.
Pages inactive:                          679475.
Pages speculative:                       295456.
Pages throttled:                              0.
Pages wired down:                        136015.
Pages purgeable:                          39980.
"Translation faults":                 139853079.
Pages copy-on-write:                    7433184.
Pages zero filled:                     69659705.
Pages reactivated:                       706288.
Pages purged:                            116452.
File-backed pages:                      1084045.
Anonymous pages:                         749327.
Pages stored in compressor:              200877.
Pages occupied by compressor:             83867.
Decompressions:                           77148.
Compressions:                            286830.
Pageins:                                4588693.
Pageouts:                                 28563.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 9041 
Pages purgeable: 39980 
Pages purged: 116452 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 858452 
Pages inactive: 679475 
Pages speculative: 295456 
Pages throttled: 0 
Pages wired down: 136015 

Compressor Stats:
Pages used by compressor: 83867 
Pages decompressed: 77148 
Pages compressed: 286830 

File I/O:
Pageins: 4588694 
Pageouts: 28563 

System-wide memory free percentage: 89%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    17Gi    18Gi    49%    427k  190M    0%   /
devfs            201Ki   201Ki     0Bi   100%     696     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    18Gi     1%       0  190M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    15Gi    18Gi    46%    2.2k  190M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   349Mi    18Gi     2%     176  190M    0%   /System/Volumes/Update
/dev/disk2s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk2s1     500Mi   6.0Mi   483Mi     2%      31  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk2s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   408Gi    18Gi    96%    3.7M  190M    2%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk1s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    17Gi    18Gi    49%    459k  190M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    17Gi    18Gi    49%    427k  190M    0%   /

```
✅ 主磁盘使用率: 49%

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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-29 13:24:11)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-29 13:02:12)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-29 13:00:22)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-29 12:58:03)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-29 08:06:41)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-28 20:11:22)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-28 19:03:16)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-28 18:05:35)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-28 15:03:55)
- `e2514301-9dc3-4ba8-9a9d-8a8fc9cc7ca0.jsonl` (更新时间: 2026-05-22 18:03:13)

## Gateway 日志异常

✅ 最近日志中未检测到明显异常

## 系统整体状态

**Top 进程**:
```
Processes: 724 total, 3 running, 721 sleeping, 3646 threads 
2026/05/29 13:30:07
Load Avg: 2.66, 2.65, 2.65 
CPU usage: 13.39% user, 13.39% sys, 73.21% idle 
SharedLibs: 1001M resident, 194M data, 460M linkedit.
MemRegions: 364927 total, 6233M resident, 825M private, 4511M shared.
PhysMem: 27G used (1999M wired, 1310M compressor), 4790M unused.
VM: 311T vsize, 5702M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 12008148/33G in, 4537733/22G out.
Disks: 5987350/140G read, 2532814/135G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID STATE    BOOSTS %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD   SYSMACH CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER           #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
71104  STExtractionServ 0.0  01:26.70 2   1   25     5056K 0B   0B    71104 1    sleeping  0[0]  0.00000 0.00000    242 62746  121 9600    6286    165198   16044   145366  15      0     0.0   0      0      0      _nsurlsessiond N/A    N/A   N/A   N/A   N/A   N/A  
69347  proactiveeventtr 0.0  00:00.05 2   1   56     2816K 0B   0B    69347 1    sleeping *0[1]  0.00000 0.00000    501 1047   142 157     51      771      379     208     5       0     0.0   0      0      0      3pigcn         N/A    N/A   N/A   N/A   N/A   N/A  
67618  RosettaUpdateSer 0.0  00:00.02 2   1   21     4208K 0B   0B    67618 1    sleeping  0[0]  0.00000 0.00000    0   833    130 70      36      462      195     91      2       0     0.0   0      0      0      root           N/A    N/A   N/A   N/A   N/A   N/A  
67544  com.apple.Mobile 0.0  14:00.33 4   1   94     52M   0B   0B    67544 1    sleeping *0[1]  0.00000 0.00000    0   291927 193 14418   6841    42892690 16577   5841604 163263  11    0.0   0      0      0      root           N/A    N/A   N/A   N/A   N/A   N/A  
67499  DPSubmissionServ 0.0  00:00.05 3   2   55     3600K 0B   0B    67499 1    sleeping  0[0]  0.00000 0.00000    501 1403   176 219     73      1530     49
```

---
*报告生成完成 @ 2026-05-29 13:30:05*
