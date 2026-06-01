#!/usr/bin/env python3
import json
import urllib.request
import urllib.parse
import sys

JIRA_HOST = "http://116.205.141.57:50008"
TOKEN = "<JIRA_BEARER_TOKEN_REDACTED>"

def jira_request(url, data=None, method=None):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    req = urllib.request.Request(url, headers=headers, data=data, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()[:500]}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Check "处理中" (status=3) assigned to huahua
print("=== 处理中 tickets assigned to huahua ===")
jql = 'project=AIWH AND status=3 AND assignee="huahua@3pigc.com"'
encoded = urllib.parse.quote(jql, safe='')
url = f"{JIRA_HOST}/rest/api/2/search?jql={encoded}&fields=key,summary,status,assignee,description&maxResults=50"
result = jira_request(url)
if result:
    print(f"Total: {result.get('total', 0)}")
    for issue in result.get('issues', []):
        fields = issue['fields']
        assignee = fields.get('assignee', {}).get('displayName') if fields.get('assignee') else "None"
        print(f"  {issue['key']}: {fields['summary']} | assignee: {assignee}")
else:
    print("No result or error")

# Check all "待办" (status=10000) unassigned
print("\n=== 待办 tickets (unassigned) ===")
jql = 'project=AIWH AND status=10000 AND assignee is EMPTY'
encoded = urllib.parse.quote(jql, safe='')
url = f"{JIRA_HOST}/rest/api/2/search?jql={encoded}&fields=key,summary,status,assignee,description&maxResults=50"
result = jira_request(url)
if result:
    print(f"Total: {result.get('total', 0)}")
    for issue in result.get('issues', []):
        fields = issue['fields']
        assignee = fields.get('assignee', {}).get('displayName') if fields.get('assignee') else "None"
        print(f"  {issue['key']}: {fields['summary']} | assignee: {assignee}")
else:
    print("No result or error")

# Check all non-done tickets in AIWH
print("\n=== All non-done tickets in AIWH ===")
jql = 'project=AIWH AND status!=10001'
encoded = urllib.parse.quote(jql, safe='')
url = f"{JIRA_HOST}/rest/api/2/search?jql={encoded}&fields=key,summary,status,assignee,description&maxResults=50"
result = jira_request(url)
if result:
    print(f"Total: {result.get('total', 0)}")
    for issue in result.get('issues', []):
        fields = issue['fields']
        assignee = fields.get('assignee', {}).get('displayName') if fields.get('assignee') else "None"
        print(f"  {issue['key']}: {fields['summary']} | status: {fields['status']['name']} | assignee: {assignee}")
else:
    print("No result or error")
