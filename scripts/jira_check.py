#!/usr/bin/env python3
import os, json, urllib.request, urllib.error, urllib.parse

AUTH_TOKEN = "<JIRA_BEARER_TOKEN_REDACTED>"
EMAIL = "huahua@3pigc.com"
JIRA_BASE = "http://116.205.141.57:50008/rest/api/2"

def jira_query(jql):
    url = f"{JIRA_BASE}/search?jql={urllib.parse.quote(jql)}&fields=key,summary,status,description,assignee,issuetype&maxResults=20"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Accept": "application/json"
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.read().decode()[:500]}"}
    except Exception as e:
        return {"error": str(e)}

def main():
    # 1. 检查处理中
    jql1 = 'project = AIWH AND status = "In Progress" AND assignee = currentUser()'
    r1 = jira_query(jql1)
    print("=== IN PROGRESS ===")
    print(json.dumps(r1, indent=2, ensure_ascii=False))

    # 2. 检查待领取
    jql2 = 'project = AIWH AND status = "Selected for Development" AND assignee is EMPTY'
    r2 = jira_query(jql2)
    print("\n=== SELECTED FOR DEV ===")
    print(json.dumps(r2, indent=2, ensure_ascii=False))

    # 3. 额外检查：未分配（即使状态不同）
    jql3 = 'project = AIWH AND assignee is EMPTY'
    r3 = jira_query(jql3)
    print("\n=== ALL UNASSIGNED ===")
    print(json.dumps(r3, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
