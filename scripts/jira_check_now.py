#!/usr/bin/env python3
import json
import urllib.parse
import urllib.request

BASE_URL = "http://116.205.141.57:50008/rest/api/2"
TOKEN = "<JIRA_BEARER_TOKEN_REDACTED>"

def jira_search(jql, fields="key,summary,status,assignee,description"):
    url = f"{BASE_URL}/search?jql={urllib.parse.quote(jql)}&fields={fields}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

# 1. Check in-progress tickets assigned to huahua
print("=== In Progress (huahua) ===")
result = jira_search('project=AIWH AND status="In Progress" AND assignee=huahua')
print(f"Total: {result['total']}")
for issue in result['issues']:
    print(f"  {issue['key']}: {issue['fields']['summary']}")

# 2. Check Selected for Development unassigned
print("\n=== Selected for Development (unassigned) ===")
result = jira_search('project=AIWH AND status="Selected for Development" AND assignee is EMPTY')
print(f"Total: {result['total']}")
for issue in result['issues']:
    print(f"  {issue['key']}: {issue['fields']['summary']}")

# 3. Check all unassigned non-done tickets
print("\n=== All unassigned non-done ===")
result = jira_search('project=AIWH AND status!=10001 AND assignee is EMPTY ORDER BY priority DESC, created ASC')
print(f"Total: {result['total']}")
for issue in result['issues']:
    status = issue['fields']['status']['name']
    print(f"  {issue['key']}: [{status}] {issue['fields']['summary']}")
