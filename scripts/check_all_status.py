import requests
from collections import defaultdict

TOKEN = '<JIRA_BEARER_TOKEN_REDACTED>'
BASE = 'http://116.205.141.57:50008'
headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}

r = requests.get(f'{BASE}/rest/api/2/search', headers=headers, params={
    'jql': 'project=AIWH',
    'fields': 'key,summary,status,assignee',
    'maxResults': 200
})
data = r.json()

status_map = defaultdict(list)
for issue in data.get('issues', []):
    status_name = issue['fields']['status']['name']
    assignee = issue['fields']['assignee']['displayName'] if issue['fields']['assignee'] else 'EMPTY'
    status_map[status_name].append(f"{issue['key']} ({assignee})")

for status, tickets in sorted(status_map.items()):
    print(f'[{status}] ({len(tickets)})')
    for t in tickets:
        print(f'  {t}')
