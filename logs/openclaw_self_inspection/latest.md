# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-30 02:00:08 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `2:00  up 18:16, 5 users, load averages: 2.07 1.67 1.56`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                              183731.
Pages active:                            846071.
Pages inactive:                          773783.
Pages speculative:                        71243.
Pages throttled:                              0.
Pages wired down:                        124125.
Pages purgeable:                          75492.
"Translation faults":                 364772878.
Pages copy-on-write:                   20806484.
Pages zero filled:                    191918518.
Pages reactivated:                      1668017.
Pages purged:                            749273.
File-backed pages:                       886773.
Anonymous pages:                         804324.
Pages stored in compressor:              164681.
Pages occupied by compressor:             63570.
Decompressions:                          318869.
Compressions:                            845300.
Pageins:                                8728313.
Pageouts:                                 53134.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 183699 
Pages purgeable: 75492 
Pages purged: 749273 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 846067 
Pages inactive: 773788 
Pages speculative: 71243 
Pages throttled: 0 
Pages wired down: 124125 

Compressor Stats:
Pages used by compressor: 63570 
Pages decompressed: 318869 
Pages compressed: 845300 

File I/O:
Pageins: 8728314 
Pageouts: 53134 

System-wide memory free percentage: 90%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    17Gi    36Gi    33%    427k  373M    0%   /
devfs            199Ki   199Ki     0Bi   100%     690     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    36Gi     1%       0  373M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    15Gi    36Gi    30%    2.0k  373M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   349Mi    36Gi     1%     176  373M    0%   /System/Volumes/Update
/dev/disk2s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk2s1     500Mi   6.0Mi   483Mi     2%      31  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk2s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   390Gi    36Gi    92%    3.7M  373M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk1s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    17Gi    36Gi    33%    459k  373M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    17Gi    36Gi    33%    427k  373M    0%   /

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
File logs: /tmp/openclaw/openclaw-2026-05-30.log
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-30 01:59:40)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-30 01:32:36)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-30 01:01:20)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-30 01:00:23)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-29 20:00:29)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-29 19:04:06)
- `e2514301-9dc3-4ba8-9a9d-8a8fc9cc7ca0.jsonl` (更新时间: 2026-05-29 18:02:33)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-29 18:02:33)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-29 15:01:12)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-29 08:06:41)

## Gateway 日志异常

⚠️ `openclaw-2026-05-30.log` 中发现异常:
  - `{"0":"{\"subsystem\":\"diagnostic\"}","1":"message processed: channel=cron chatId=unknown messageId=unknown sessionId=31`
  - `{"0":"[tools] read failed: ENOENT: no such file or directory, access '/Users/3pigcn/clawd/memory/jira-config.json' raw_p`
  - `{"0":"[tools] read failed: ENOENT: no such file or directory, access '/Users/3pigcn/clawd/memory/jira-config.json' raw_p`

## 系统整体状态

**Top 进程**:
```
Processes: 800 total, 2 running, 798 sleeping, 3392 threads 
2026/05/30 02:00:10
Load Avg: 2.06, 1.68, 1.56 
CPU usage: 1.47% user, 9.31% sys, 89.21% idle 
SharedLibs: 1124M resident, 172M data, 346M linkedit.
MemRegions: 298972 total, 7248M resident, 805M private, 3200M shared.
PhysMem: 28G used (1884M wired, 993M compressor), 3982M unused.
VM: 331T vsize, 5702M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 17090833/36G in, 9831496/24G out.
Disks: 10072652/221G read, 5127398/243G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG  CMPRS PGRP  PPID STATE    BOOSTS   %CPU_ME %CPU_OTHRS UID FAULTS  COW MSGSENT  MSGRECV SYSBSD  SYSMACH  CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER   #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
98539  VTDecoderXPCServ 0.0  02:15.01 6   1   111    8448K 0B    0B    98539 1    sleeping *0[359]  0.00000 0.00000    501 2762347 191 4893748  2463886 2358404 6343741  1232183 2       3     0.0   0      0      40     3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
98538  com.apple.ColorS 0.0  00:00.00 2   1   27     1600K 0B    0B    98538 1    sleeping *0[1]    0.00000 0.00000    501 583     114 107      40      423     236      43      2       0     0.0   0      0      0      3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
98537  DisplaysExt      0.0  11:47.95 13  10  416    52M   3264K 0B    98537 1    sleeping  0[1812] 0.00000 0.00000    501 3988131 485 12220474 6070405 2486674 12980440 2076824 18      12622 0.0   0      0      40     3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
98530  ClassroomSetting 0.0  00:00.25 4   2   167    9345K 0B    0B    98530 1    sleeping *49[6]   0.00000 0.00000    501 2787    228 3752     2213    16415   13939    5454    17      35    0.0   0      0      40     3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
98529  FamilySettings   0.0  00:00.44 4   2   246    13M   0B    0B    98529 1    sleeping  0[1529] 0.00000 0.00000    501 4341    346 4385     2240    21598   14882    7724  
```

---
*报告生成完成 @ 2026-05-30 02:00:08*
