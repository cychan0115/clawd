#!/usr/bin/env python3
import os
import sys
import json
import urllib.parse

JIRA_HOST = os.environ.get("JIRA_HOST", "http://116.205.141.57:50008")
JIRA_TOKEN = os.environ.get("JIRA_TOKEN", "")
JIRA_USER = os.environ.get("JIRA_USER", "huahua@3pigc.com")
PROJECT = os.environ.get("JIRA_PROJECT", "AIWH")

def jira_api(method, endpoint, data=None):
    url = f"{JIRA_HOST}{endpoint}"
    headers = ["-H", f"Authorization: Bearer {JIRA_TOKEN}", "-H", "Content-Type: application/json"]
    if method == "GET":
        cmd = ["curl", "-s", "-X", "GET"] + headers + [url]
    elif method == "POST":
        cmd = ["curl", "-s", "-X", "POST"] + headers + ["-d", json.dumps(data, ensure_ascii=False)] + [url]
    elif method == "PUT":
        cmd = ["curl", "-s", "-X", "PUT"] + headers + ["-d", json.dumps(data, ensure_ascii=False)] + [url]
    else:
        raise ValueError(f"Unknown method: {method}")
    result = os.popen(" ".join(cmd)).read()
    try:
        return json.loads(result) if result else {}
    except:
        return {"raw": result}

def search_issues(jql, fields="summary,status,assignee,description"):
    encoded_jql = urllib.parse.quote(jql)
    endpoint = f"/rest/api/2/search?jql={encoded_jql}&fields={fields}"
    return jira_api("GET", endpoint)

if __name__ == "__main__":
    if not JIRA_TOKEN:
        print("Error: JIRA_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    print("=== 1. 处理中 + assignee=huahua ===")
    in_progress = search_issues(f'project={PROJECT} AND status="处理中" AND assignee=huahua')
    issues = in_progress.get("issues", [])
    print(f"Found {len(issues)} in-progress ticket(s)")
    for issue in issues:
        key = issue["key"]
        print(f"  - {key}: {issue['fields']['summary']}")

    print("\n=== 2. Selected for Development + assignee EMPTY ===")
    selected = search_issues(f'project={PROJECT} AND status="Selected for Development" AND assignee is EMPTY')
    issues = selected.get("issues", [])
    print(f"Found {len(issues)} selected ticket(s)")
    for issue in issues:
        key = issue["key"]
        print(f"  - {key}: {issue['fields']['summary']}")

    print("\n=== 3. ALL AIWH tickets (非完成) ===")
    all_issues = search_issues(f'project={PROJECT} AND status!=完成')
    issues = all_issues.get("issues", [])
    print(f"Found {len(issues)} non-done ticket(s)")
    for issue in issues:
        key = issue["key"]
        status = issue['fields']['status']['name']
        assignee = issue['fields'].get('assignee',{})
        assignee_name = assignee.get('displayName','EMPTY') if assignee else 'EMPTY'
        print(f"  - {key}: [{status}] assignee={assignee_name} | {issue['fields']['summary']}")
