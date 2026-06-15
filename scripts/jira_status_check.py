#!/usr/bin/env python3
import requests, urllib.parse

base = 'http://116.205.141.57:50008/rest/api/2/search'
token = os.environ.get('JIRA_TOKEN', '')
if not token:
    print('Please set JIRA_TOKEN environment variable')
    sys.exit(1)
headers = {'Authorization': f'Bearer {token}'}

jql = 'project=AIWH'
url = f'{base}?jql={urllib.parse.quote(jql)}&fields=summary,status,assignee&maxResults=100'
resp = requests.get(url, headers=headers)
data = resp.json()
print(f"总 ticket 数: {data['total']}")

from collections import Counter
status_counts = Counter()
for issue in data['issues'][:50]:
    status = issue['fields']['status']['name']
    status_counts[status] += 1

for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
    print(f'  {status}: {count}')
