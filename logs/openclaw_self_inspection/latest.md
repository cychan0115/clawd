# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-29 17:30:16 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `17:30  up  9:46, 6 users, load averages: 8.12 10.15 11.31`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                               73374.
Pages active:                            842774.
Pages inactive:                          829099.
Pages speculative:                        56734.
Pages throttled:                              0.
Pages wired down:                        145189.
Pages purgeable:                          64985.
"Translation faults":                 242331850.
Pages copy-on-write:                   12963636.
Pages zero filled:                    131385399.
Pages reactivated:                      1083808.
Pages purged:                            157619.
File-backed pages:                      1002322.
Anonymous pages:                         726285.
Pages stored in compressor:              278318.
Pages occupied by compressor:            115383.
Decompressions:                          147132.
Compressions:                            456576.
Pageins:                                6443861.
Pageouts:                                 35616.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 73091 
Pages purgeable: 64985 
Pages purged: 157619 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 842790 
Pages inactive: 829099 
Pages speculative: 56734 
Pages throttled: 0 
Pages wired down: 145189 

Compressor Stats:
Pages used by compressor: 115383 
Pages decompressed: 147132 
Pages compressed: 456576 

File I/O:
Pageins: 6443863 
Pageouts: 35616 

System-wide memory free percentage: 87%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    17Gi    33Gi    34%    427k  351M    0%   /
devfs            201Ki   201Ki     0Bi   100%     696     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    33Gi     1%       0  351M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    15Gi    33Gi    31%    2.2k  351M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   349Mi    33Gi     2%     176  351M    0%   /System/Volumes/Update
/dev/disk2s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk2s1     500Mi   6.0Mi   483Mi     2%      31  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk2s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   392Gi    33Gi    93%    3.7M  351M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk1s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    17Gi    33Gi    34%    459k  351M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    17Gi    33Gi    34%    427k  351M    0%   /

```
✅ 主磁盘使用率: 34%

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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-29 17:24:14)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-29 17:03:02)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-29 17:01:04)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-29 17:00:34)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-29 15:01:12)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-29 08:06:41)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-28 20:11:22)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-28 19:03:16)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-28 18:05:35)
- `e2514301-9dc3-4ba8-9a9d-8a8fc9cc7ca0.jsonl` (更新时间: 2026-05-22 18:03:13)

## Gateway 日志异常

✅ 最近日志中未检测到明显异常

## 系统整体状态

**Top 进程**:
```
Processes: 768 total, 5 running, 763 sleeping, 3829 threads 
2026/05/29 17:30:17
Load Avg: 8.12, 10.15, 11.31 
CPU usage: 40.90% user, 17.76% sys, 41.32% idle 
SharedLibs: 1027M resident, 192M data, 452M linkedit.
MemRegions: 377968 total, 6870M resident, 652M private, 3311M shared.
PhysMem: 30G used (2418M wired, 1803M compressor), 1984M unused.
VM: 328T vsize, 5702M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 12994651/33G in, 5656143/22G out.
Disks: 8506698/183G read, 3983400/196G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID STATE    BOOSTS %CPU_ME %CPU_OTHRS UID FAULTS COW MSGSENT MSGRECV SYSBSD   SYSMACH CSW     PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER           #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
93048  IMTransferAgent  0.0  00:00.29 3   1   91     4848K 48K  0B    93048 1    sleeping *4[1]  0.00000 0.00000    501 2270   211 635     255     9270     2377    2209    961     0     0.0   0      0      0      3pigcn         N/A    N/A   N/A   N/A   N/A   N/A  
71104  STExtractionServ 0.0  01:26.70 2   1   25     5216K 0B   4768K 71104 1    sleeping  0[0]  0.00000 0.00000    242 62746  121 9600    6286    165198   16044   145366  15      0     0.0   0      0      0      _nsurlsessiond N/A    N/A   N/A   N/A   N/A   N/A  
69347  proactiveeventtr 0.0  00:00.05 2   1   56     3264K 0B   2400K 69347 1    sleeping *0[1]  0.00000 0.00000    501 1047   142 157     51      771      379     208     5       0     0.0   0      0      0      3pigcn         N/A    N/A   N/A   N/A   N/A   N/A  
67618  RosettaUpdateSer 0.0  00:00.02 2   1   21     4224K 0B   3840K 67618 1    sleeping  0[0]  0.00000 0.00000    0   833    130 70      36      462      195     91      2       0     0.0   0      0      0      root           N/A    N/A   N/A   N/A   N/A   N/A  
67544  com.apple.Mobile 0.0  14:00.41 4   1   94     56M   0B   14M   67544 1    sleeping *0[1]  0.00000 0.00000    0   292058 193 14620   6949    42895303 
```

---
*报告生成完成 @ 2026-05-29 17:30:16*
