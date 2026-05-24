#!/usr/bin/env python3
"""Jira task query helper for huahua"""
import json, urllib.request, urllib.parse, sys

TOKEN = "<JIRA_BEARER_TOKEN_REDACTED>"
BASE = "http://116.205.141.57:50008/rest/api/2"

def jira_get(path, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return {"error": str(e)}

def jira_post(path, data, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    body = json.dumps(data).encode()
    req = urllib.request.Request(url, data=body, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": str(e), "status": e.code, "body": e.read().decode()}
    except Exception as e:
        return {"error": str(e)}

# 1. 查询处理中的 ticket (assignee=huahua, status=处理中 id=3)
print("=== 处理中 tickets (assignee=huahua) ===")
in_progress = jira_get("/search", {
    "jql": "project=AIWH AND status=3 AND assignee=huahua",
    "fields": "key,summary,status,assignee,description"
})
print(json.dumps(in_progress, ensure_ascii=False, indent=2))

print("\n=== 待领取 tickets (Selected for Development, EMPTY assignee) ===")
todo = jira_get("/search", {
    "jql": "project=AIWH AND status=10201 AND assignee is EMPTY",
    "fields": "key,summary,status,assignee,description"
})
print(json.dumps(todo, ensure_ascii=False, indent=2))
