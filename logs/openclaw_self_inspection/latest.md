# MINI2 + OpenClaw 自巡检报告

**时间**: 2026-05-26 14:33:33 (Asia/Shanghai)

**主机**: mini2 (Mac mini)

**触发**: cron job `73bbdaca-9c48-41d7-a333-1c3e2d112c95`


## macOS 主机资源

**负载**: `14:33  up 8 days, 17:25, 7 users, load averages: 5.12 5.52 5.27`
**内存 (vm_stat)**:
```
Mach Virtual Memory Statistics: (page size of 16384 bytes)
Pages free:                              145583.
Pages active:                            687158.
Pages inactive:                          635566.
Pages speculative:                        60016.
Pages throttled:                              0.
Pages wired down:                        418679.
Pages purgeable:                          23187.
"Translation faults":                6709301927.
Pages copy-on-write:                  183914577.
Pages zero filled:                   4460894305.
Pages reactivated:                     23573012.
Pages purged:                           2283396.
File-backed pages:                       422194.
Anonymous pages:                         960546.
Pages stored in compressor:              305219.
Pages occupied by compressor:            115508.
Decompressions:                         7264341.
Compressions:                          16679774.
Pageins:                               55543920.
Pageouts:                               1508663.
Swapins:                                      0.
Swapouts:                                     0.

```
**内存压力**:
```
The system has 34359738368 (2097152 pages with a page size of 16384).

Stats: 
Pages free: 145560 
Pages purgeable: 23187 
Pages purged: 2283396 

Swap I/O:
Swapins: 0 
Swapouts: 0 

Page Q counts:
Pages active: 687163 
Pages inactive: 635567 
Pages speculative: 60022 
Pages throttled: 0 
Pages wired down: 418681 

Compressor Stats:
Pages used by compressor: 115508 
Pages decompressed: 7264341 
Pages compressed: 16679774 

File I/O:
Pageins: 55543921 
Pageouts: 1508663 

System-wide memory free percentage: 74%

```

## 磁盘空间

```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    26Gi    35%    426k  271M    0%   /
devfs            201Ki   201Ki     0Bi   100%     696     0  100%   /dev
/dev/disk3s6     460Gi    24Ki    26Gi     1%       0  271M    0%   /System/Volumes/VM
/dev/disk3s2     460Gi    13Gi    26Gi    34%    1.8k  271M    0%   /System/Volumes/Preboot
/dev/disk3s4     460Gi   691Mi    26Gi     3%     301  271M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   483Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.8Mi   483Mi     2%      37  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   716Ki   483Mi     1%      80  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     460Gi   405Gi    26Gi    95%    3.7M  271M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   2.1Gi   2.9Gi    43%      60   30M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     460Gi    14Gi    26Gi    35%    427k  271M    0%   /System/Volumes/Update/mnt1

```
**主磁盘 (/)**:
```
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   460Gi    14Gi    26Gi    35%    426k  271M    0%   /

```
✅ 主磁盘使用率: 35%

## OpenClaw 进程

✅ gateway: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 97828)
✅ agent: 运行中 (PIDs: 9898, 9985, 54907, 54914, 54915, 54917, 54920, 54921, 54923, 56552, 64656, 97828)
✅ browser: 运行中 (通过 ps 确认)

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
File logs: /tmp/openclaw/openclaw-2026-05-26.log
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
- `8d0227c6-23ec-434c-802a-97bdb590dc1f.jsonl` (更新时间: 2026-05-26 14:33:23)
- `078443c8-c048-4e69-8dab-eb99c185567b.jsonl` (更新时间: 2026-05-26 14:02:59)
- `73bbdaca-9c48-41d7-a333-1c3e2d112c95.jsonl` (更新时间: 2026-05-26 14:02:47)
- `e3a596af-d4b9-40f1-ae36-d6208dc3e55b.jsonl` (更新时间: 2026-05-26 12:54:25)
- `c25d0bde-a2bc-49c7-9037-729ddf8a1576.jsonl` (更新时间: 2026-05-26 08:07:37)
- `5bc40a82-ab3e-4082-ac5a-df1048f3860d.jsonl` (更新时间: 2026-05-25 20:02:32)
- `f24e53d3-28d8-4c33-8e8f-bd36d6e244c0.jsonl` (更新时间: 2026-05-25 19:03:11)
- `15a38810-d37b-4084-be84-df02e0e78cb4.jsonl` (更新时间: 2026-05-25 18:02:58)
- `4ca01174-86be-4bfe-abba-f00e41eaf07d.jsonl` (更新时间: 2026-05-25 15:05:39)
- `e2514301-9dc3-4ba8-9a9d-8a8fc9cc7ca0.jsonl` (更新时间: 2026-05-22 18:03:13)

## Gateway 日志异常

⚠️ `openclaw-2026-05-26.log` 中发现异常:
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"[tools] edit failed: Could not find the exact text in /Users/3pigcn/clawd/wing_recovery_alert.md. The old text mus`
  - `{"0":"[tools] edit failed: Could not find the exact text in /Users/3pigcn/clawd/wing_recovery_alert.md. The old text mus`
⚠️ `openclaw-2026-05-25.log` 中发现异常:
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`
  - `{"0":"{\"subsystem\":\"bundle-mcp\"}","1":"failed to start server \"chrome-devtools\" (npx -y chrome-devtools-mcp@latest`

## 系统整体状态

**Top 进程**:
```
Processes: 631 total, 4 running, 627 sleeping, 2777 threads 
2026/05/26 14:33:35
Load Avg: 5.12, 5.52, 5.27 
CPU usage: 24.62% user, 8.95% sys, 66.41% idle 
SharedLibs: 899M resident, 129M data, 75M linkedit.
MemRegions: 166812 total, 6333M resident, 444M private, 7942M shared.
PhysMem: 28G used (6546M wired, 1805M compressor), 3170M unused.
VM: 257T vsize, 5703M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 73652658/88G in, 61833164/62G out.
Disks: 81813086/1229G read, 52691322/2381G written.

PID    COMMAND          %CPU TIME     #TH #WQ #PORTS MEM   PURG CMPRS PGRP  PPID  STATE    BOOSTS   %CPU_ME %CPU_OTHRS UID FAULTS COW  MSGSENT MSGRECV SYSBSD SYSMACH CSW   PAGEINS IDLEW POWER INSTRS CYCLES JETPRI USER   #MREGS RPRVT VPRVT VSIZE KPRVT KSHRD
99060  ContainerMetadat 0.0  00:00.30 2   1   60     4208K 0B   3760K 99060 1     sleeping *0[6]    0.00000 0.00000    501 3233   159  1074    571     6878   1345    1223  4       0     0.0   0      0      0      3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
98518  com.apple.Safari 0.0  00:04.27 2   1   58     6577K 0B   4208K 98518 1     sleeping *0[1010] 0.00000 0.00000    501 28726  185  14322   9868    364090 113111  83346 93      296   0.0   0      0      0      3pigcn N/A    N/A   N/A   N/A   N/A   N/A  
97907  top              0.0  00:00.13 1/1 0   16     3984K 0B   0B    53376 97845 running  *0[1]    0.00000 0.00000    0   1169   113  372026  186012  3336   190742  7     5       0     0.0   0      0      180    root   N/A    N/A   N/A   N/A   N/A   N/A  
97905  sshd-session     0.0  00:00.00 1   0   18     1840K 0B   0B    97904 97904 sleeping *0[1]    0.00000 0.00000    75  196    60   26      12      61     62      17    0       0     0.0   0      0      180    _sshd  N/A    N/A   N/A   N/A   N/A   N/A  
97904  sshd-session     0.0  00:00.02 1   0   22     2432K 0B   0B    97904 1     sleeping *0[1]    0.00000 0.00000    0   1416   317  119     44      877    401     44    4       0     0.0   0   
```

---
*报告生成完成 @ 2026-05-26 14:33:33*
