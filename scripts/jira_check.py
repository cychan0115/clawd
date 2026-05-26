#!/usr/bin/env python3
import requests
import json
import urllib.parse

TOKEN = "<JIRA_BEARER_TOKEN_REDACTED>"
JIRA_BASE = "http://116.205.141.57:50008"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# 1. Check in-progress tickets assigned to huahua
jql1 = "project = AIWH AND status = 'In Progress' AND assignee = huahua"
params1 = {
    "jql": jql1,
    "fields": "key,summary,status,assignee,description"
}
print("=== In Progress tickets ===")
r1 = requests.get(f"{JIRA_BASE}/rest/api/2/search", headers=headers, params=params1, timeout=30)
print(f"Status: {r1.status_code}")
if r1.status_code == 200:
    data1 = r1.json()
    print(f"Total: {data1['total']}")
    for issue in data1['issues']:
        print(f"- {issue['key']}: {issue['fields']['summary']}")
else:
    print(r1.text[:500])

# 2. Check available tickets
jql2 = "project = AIWH AND status = 'Selected for Development' AND assignee is EMPTY"
params2 = {
    "jql": jql2,
    "fields": "key,summary,status,assignee,description"
}
print("\n=== Available tickets ===")
r2 = requests.get(f"{JIRA_BASE}/rest/api/2/search", headers=headers, params=params2, timeout=30)
print(f"Status: {r2.status_code}")
if r2.status_code == 200:
    data2 = r2.json()
    print(f"Total: {data2['total']}")
    for issue in data2['issues']:
        print(f"- {issue['key']}: {issue['fields']['summary']}")
else:
    print(r2.text[:500])

# 3. Check all unassigned tickets
jql3 = "project = AIWH AND status != 'Done' AND status != 'Closed'"
params3 = {
    "jql": jql3,
    "fields": "key,summary,status,assignee"
}
print("\n=== All open tickets ===")
r3 = requests.get(f"{JIRA_BASE}/rest/api/2/search", headers=headers, params=params3, timeout=30)
print(f"Status: {r3.status_code}")
if r3.status_code == 200:
    data3 = r3.json()
    print(f"Total: {data3['total']}")
    for issue in data3['issues']:
        fields = issue['fields']
        assignee = fields.get('assignee', {})
        assignee_name = assignee.get('displayName', 'UNASSIGNED') if assignee else 'UNASSIGNED'
        status = fields.get('status', {}).get('name', 'UNKNOWN')
        print(f"- {issue['key']}: [{status}] {fields['summary']} (assignee: {assignee_name})")
else:
    print(r3.text[:500])
