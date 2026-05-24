#!/usr/bin/env python3
"""Jira helper for huahua"""
import requests, json, sys, os

HOST = "http://116.205.141.57:50008"
TOKEN = "<JIRA_BEARER_TOKEN_REDACTED>"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def search(jql, fields="key,summary,status,assignee,description", max_results=50):
    url = f"{HOST}/rest/api/2/search"
    params = {"jql": jql, "fields": fields, "maxResults": max_results}
    r = requests.get(url, headers=HEADERS, params=params)
    return r.json()

def get_issue(key, fields="key,summary,status,assignee,description,comment"):
    url = f"{HOST}/rest/api/2/issue/{key}"
    params = {"fields": fields}
    r = requests.get(url, headers=HEADERS, params=params)
    return r.json()

def assign(key, username="huahua"):
    url = f"{HOST}/rest/api/2/issue/{key}/assignee"
    payload = {"name": username}
    r = requests.put(url, headers=HEADERS, json=payload)
    return r.status_code, r.text

def transition(key, transition_id):
    url = f"{HOST}/rest/api/2/issue/{key}/transitions"
    payload = {"transition": {"id": transition_id}}
    r = requests.post(url, headers=HEADERS, json=payload)
    return r.status_code, r.text

def comment(key, body):
    url = f"{HOST}/rest/api/2/issue/{key}/comment"
    payload = {"body": body}
    r = requests.post(url, headers=HEADERS, json=payload)
    return r.status_code, r.json()

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "search":
        jql = sys.argv[2]
        print(json.dumps(search(jql), indent=2, ensure_ascii=False))
    elif cmd == "get":
        key = sys.argv[2]
        print(json.dumps(get_issue(key), indent=2, ensure_ascii=False))
    elif cmd == "assign":
        key = sys.argv[2]
        print(assign(key))
    elif cmd == "transition":
        key = sys.argv[2]
        tid = sys.argv[3]
        print(transition(key, tid))
    elif cmd == "comment":
        key = sys.argv[2]
        body = sys.argv[3]
        print(comment(key, body))
    else:
        print("Usage: jira_helper.py search|get|assign|transition|comment ...")
