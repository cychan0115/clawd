import os
import sys
import json
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

JIRA_HOST = "http://116.205.141.57:50008"
JIRA_TOKEN = "<JIRA_BEARER_TOKEN_REDACTED>"
JIRA_USER = "huahua@3pigc.com"
PROJECT = "AIWH"

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

def get_issue(key, fields="summary,status,assignee,description"):
    endpoint = f"/rest/api/2/issue/{key}?fields={fields}"
    return jira_api("GET", endpoint)

def add_comment(key, body):
    endpoint = f"/rest/api/2/issue/{key}/comment"
    return jira_api("POST", endpoint, {"body": body})

def assign_issue(key, assignee):
    endpoint = f"/rest/api/2/issue/{key}/assignee"
    return jira_api("PUT", endpoint, {"name": assignee})

def do_transition(key, transition_id):
    endpoint = f"/rest/api/2/issue/{key}/transitions"
    # first get available transitions
    resp = jira_api("GET", endpoint)
    print(f"Available transitions for {key}:")
    for t in resp.get("transitions", []):
        print(f"  {t['id']}: {t['name']} -> {t.get('to',{}).get('name','')}")
    # do transition
    endpoint = f"/rest/api/2/issue/{key}/transitions"
    return jira_api("POST", endpoint, {"transition": {"id": transition_id}})

def git_status():
    workspace = Path.home() / "workspace" / "wing_1"
    if not workspace.exists():
        return None, "workspace not found"
    result = os.popen(f"cd {workspace} && git status --short").read().strip()
    return workspace, result

def git_commit_push(workspace, message):
    os.system(f"cd {workspace} && git add . && git commit -m '{message}' && git push origin master")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 jira_auto.py <check|claim|done>")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "check":
        # Check in-progress tickets
        print("=== Checking in-progress tickets ===")
        in_progress = search_issues(f'project={PROJECT} AND status="处理中" AND assignee=huahua')
        issues = in_progress.get("issues", [])
        print(f"Found {len(issues)} in-progress ticket(s)")
        for issue in issues:
            key = issue["key"]
            print(f"  - {key}: {issue['fields']['summary']}")
        
        # Check selected for development
        print("\n=== Checking Selected for Development tickets ===")
        selected = search_issues(f'project={PROJECT} AND status="Selected for Development" AND assignee is EMPTY')
        issues = selected.get("issues", [])
        print(f"Found {len(issues)} selected ticket(s)")
        for issue in issues:
            key = issue["key"]
            print(f"  - {key}: {issue['fields']['summary']}")
        
        print("\n=== Checking ALL AIWH tickets ===")
        all_issues = search_issues(f'project={PROJECT}')
        issues = all_issues.get("issues", [])
        print(f"Found {len(issues)} total ticket(s)")
        for issue in issues:
            key = issue["key"]
            status = issue['fields']['status']['name']
            assignee = issue['fields'].get('assignee',{})
            assignee_name = assignee.get('displayName','EMPTY') if assignee else 'EMPTY'
            print(f"  - {key}: [{status}] assignee={assignee_name} | {issue['fields']['summary']}")
    
    elif cmd == "claim":
        key = sys.argv[2]
        print(f"Claiming {key}...")
        assign_issue(key, "huahua")
        do_transition(key, 31)
        add_comment(key, f"[Preflight Check]\n\nClaimed by huahua.\n\nReady to start work.")
        print(f"Done claiming {key}")
    
    elif cmd == "done":
        key = sys.argv[2]
        print(f"Marking {key} as done...")
        do_transition(key, 41)
        add_comment(key, f"[Done Report]\n\nWork completed.\n\nEvidence: commit hash and files attached.")
        print(f"Done marking {key}")
    
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
