#!/usr/bin/env python3
"""
追踪titan007.com盘路连续7次模式
- 7连胜 / 7连败
- 7连赢盘 / 7连输盘  
- 7连大球 / 7连小球
"""

import requests, re
from concurrent.futures import ThreadPoolExecutor, as_completed

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Referer': 'https://live.titan007.com/',
}

session = requests.Session()

# 从文件读取比赛ID
import json
with open('/Users/3pigcn/clawd/match_ids.json', 'r') as f:
    ids = json.load(f)
seen_ids = set(ids)
print(f"🔍 从文件加载 {len(seen_ids)} 个比赛ID")

# ============ 盘路计算逻辑（从panlu.js翻译） ============
def calc_result(h_score, g_score):
    """从主队视角：0=胜, 1=平, 2=负"""
    if h_score > g_score: return 0
    elif h_score == g_score: return 1
    else: return 2

def calc_pan_result(h_score, g_score, handicap):
    """从主队视角：0=赢盘, 1=走, 2=输盘"""
    if h_score - handicap > g_score: return 0
    elif abs((h_score - handicap) - g_score) < 0.001: return 1
    else: return 2

def calc_big_result(h_score, g_score, total_str):
    """0=大球, 1=走, 2=小球, -1=无数据"""
    if not total_str or total_str == '': return -1
    try:
        t = float(total_str)
        total = h_score + g_score
        if total > t: return 0
        elif abs(total - t) < 0.001: return 1
        else: return 2
    except:
        return -1

def reversal(v):
    """客队视角反转：0↔2, 1不变"""
    if v == 0: return 2
    elif v == 2: return 0
    else: return 1

RESULT_VIEW = ['胜', '平', '负']
PAN_VIEW = ['赢', '走', '输']
BIG_VIEW = ['', '大', '走', '小']  # 索引 = bigResult + 1

def get_team_data(mid):
    """访问panlu页面，提取两队盘路数据"""
    url = f'http://bf.titan007.com/panlu/{mid}cn.htm'
    try:
        r = session.get(url, headers=HEADERS, timeout=10)
        r.encoding = 'gbk'
        text = r.text
        
        # 提取 hometeamid, guestteamid, sclass
        m = re.search(r"var\s+hometeamid\s*=\s*(\d+)\s*,\s*guestteamid\s*=\s*(\d+)\s*,\s*sclass\s*=\s*'([^']*)'", text)
        if not m:
            return []
        hometeamid = int(m.group(1))
        guestteamid = int(m.group(2))
        sclass = m.group(3)
        
        # 提取所有 a[N]=[...] 数组
        # 格式: a[0]=[2826442,'印尼超','#5F9203','26-05-17 20:00','永亚卡达','马都拉联',19038,26684,2,1,2,0,0.5,1,0,2.5];
        # 字段: 0=id, 1=联赛, 2=color, 3=时间, 4=主队, 5=客队, 6=主队ID, 7=客队ID, 
        #       8=主队进球, 9=客队进球, 10=半场主, 11=半场客, 12=盘口, 13=主队红牌?, 14=客队红牌?, 15=大小球盘口
        
        # 更健壮的正则：匹配所有数字/字符串/浮点数组元素
        array_pattern = re.compile(
            r"a\[(\d+)\]\s*=\s*\[(.*?)\];",
            re.S
        )
        
        all_matches = []
        for arr_match in array_pattern.finditer(text):
            content = arr_match.group(2)
            # 分割数组元素（处理引号内的逗号）
            elements = []
            in_quote = False
            current = ''
            for ch in content:
                if ch == "'" and (not current or current[-1] != '\\'):
                    in_quote = not in_quote
                    current += ch
                elif ch == ',' and not in_quote:
                    elements.append(current.strip())
                    current = ''
                else:
                    current += ch
            if current.strip():
                elements.append(current.strip())
            
            if len(elements) >= 16:
                try:
                    match_id = int(elements[0])
                    league = elements[1].strip("'")
                    time_str = elements[3].strip("'")
                    home = elements[4].strip("'")
                    away = elements[5].strip("'")
                    home_id = int(elements[6])
                    guest_id = int(elements[7])
                    h_score = int(elements[8])
                    g_score = int(elements[9])
                    handicap_str = elements[12].strip()
                    # 13,14 是红牌数据（忽略）
                    total_str = elements[15].strip().strip("'")
                    
                    all_matches.append({
                        'match_id': match_id,
                        'league': league,
                        'time': time_str,
                        'home': home,
                        'away': away,
                        'home_id': home_id,
                        'guest_id': guest_id,
                        'h_score': h_score,
                        'g_score': g_score,
                        'handicap_str': handicap_str,
                        'total_str': total_str,
                    })
                except:
                    pass
        
        teams_data = []
        
        # 处理主队
        for team_id, team_name_key in [(hometeamid, 'home'), (guestteamid, 'away')]:
            results = []
            for m in all_matches:
                # vsKind=1（全部）：只要该队参与就计入
                if m['home_id'] != team_id and m['guest_id'] != team_id:
                    continue
                
                is_home = (m['home_id'] == team_id)
                
                # 计算从主队视角的结果
                result = calc_result(m['h_score'], m['g_score'])
                
                # 计算盘口
                try:
                    handicap = float(m['handicap_str'])
                except:
                    handicap = 0.0
                pan_result = calc_pan_result(m['h_score'], m['g_score'], handicap)
                
                # 计算大小球
                big_result = calc_big_result(m['h_score'], m['g_score'], m['total_str'])
                
                # 如果是客队，反转结果
                if not is_home:
                    result = reversal(result)
                    pan_result = reversal(pan_result)
                
                # 映射为文本
                result_text = RESULT_VIEW[result]
                pan_text = PAN_VIEW[pan_result]
                big_text = BIG_VIEW[big_result + 1] if big_result >= 0 else ''
                
                # 队名
                team_name = m['home'] if is_home else m['away']
                
                results.append({
                    'time': m['time'],
                    'home': m['home'],
                    'away': m['away'],
                    'score': f"{m['h_score']}-{m['g_score']}",
                    'result': result_text,
                    'panlu': pan_text,
                    'daxiao': big_text,
                    'is_home': is_home,
                    'handicap': m['handicap_str'],
                })
            
            if results:
                # 取队名（从第一条记录中）
                team_name = results[0]['home'] if results[0]['is_home'] else results[0]['away']
                teams_data.append((team_name, results))
        
        return teams_data
        
    except Exception as e:
        return []

# ============ 批量处理 ============
print("\n📊 开始批量抓取盘路数据...")
print("=" * 60)

all_teams = {}
processed = 0
errors = 0

def process_one(mid):
    try:
        teams = get_team_data(mid)
        for team_name, results in teams:
            if team_name not in all_teams or len(results) > len(all_teams[team_name]):
                all_teams[team_name] = results
        return True
    except:
        return False

# 限制为热门比赛（取前60个ID测试）
# test_ids = list(seen_ids)[:60]
# print(f"  测试处理前 {len(test_ids)} 个ID...")
test_ids = list(seen_ids)
print(f"  处理全部 {len(test_ids)} 个ID...")

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(process_one, mid): mid for mid in test_ids}
    for future in as_completed(futures):
        if future.result():
            processed += 1
        else:
            errors += 1

print(f"\n✅ 成功处理 {processed}/{len(test_ids)} 场比赛，获取到 {len(all_teams)} 支球队数据")
if errors > 0:
    print(f"   失败 {errors} 个")

# ============ 检查连续7次模式 ============
print("\n🔥 检查连续7次模式...")
print("=" * 60)

alerts = []

def check_consecutive(results, key, target_values, desc):
    """检查results中key字段是否有连续>=7次等于target_values中的值"""
    if not results or len(results) < 7:
        return
    
    streak = 0
    streak_details = []
    for r in results:
        val = r.get(key, '')
        if val in target_values:
            streak += 1
            streak_details.append(f"{r['time']} {r['home']} {r['score']} {r['away']} ({r['result']}/{r['panlu']}/{r['daxiao']}) 盘口{r['handicap']}")
        else:
            break
    
    if streak >= 7:
        return {
            'streak': streak,
            'desc': desc,
            'details': streak_details,
        }
    return None

for team_name, results in all_teams.items():
    recent = results[:15]
    
    checks = [
        ('result', ['胜'], '7连胜'),
        ('result', ['负'], '7连败'),
        ('panlu', ['赢'], '7连赢盘'),
        ('panlu', ['输'], '7连输盘'),
        ('daxiao', ['大'], '7连大球'),
        ('daxiao', ['小'], '7连小球'),
    ]
    
    for key, targets, desc in checks:
        found = check_consecutive(recent, key, targets, desc)
        if found:
            alerts.append({
                'team': team_name,
                'pattern': desc,
                'streak': found['streak'],
                'details': found['details'],
            })

# ============ 输出结果 ============
if alerts:
    print(f"\n🚨 发现 {len(alerts)} 个连续7+模式！\n")
    for a in alerts:
        print(f"【{a['pattern']}】 {a['team']} — 连续{a['streak']}场")
        for d in a['details'][:a['streak']]:
            print(f"  {d}")
        print()
else:
    print("\n😞 未发现任何连续7+模式")
    print(f"\n今天获取的 {len(all_teams)} 支球队的最近5场状态（供参考）：")
    for team_name, results in sorted(all_teams.items()):
        recent = results[:5]
        if recent:
            results_str = ' | '.join([f"{r['time']} {r['result']}{r['panlu']}{r['daxiao']}" for r in recent])
            print(f"  {team_name}: {results_str}")

print("\n" + "=" * 60)
print("检查完成！")
