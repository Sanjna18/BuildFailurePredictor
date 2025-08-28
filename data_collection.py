# data_collection.py

import requests
import git

def fetch_jenkins_builds(jenkins_url, job_name, auth):
    url = f"{jenkins_url}/job/{job_name}/api/json?tree=builds[number,result,duration,timestamp,changeSet[*]]"
    response = requests.get(url, auth=auth)
    builds = response.json().get('builds', [])
    return builds

def get_git_diff_metrics(repo_path, commit_hash):
    repo = git.Repo(repo_path)
    commit = repo.commit(commit_hash)
    diff = commit.diff(commit.parents[0] if commit.parents else None)
    added, removed, files_changed = 0, 0, len(diff)
    for d in diff:
        stats = d.diff.decode("utf-8", errors="ignore")
        added += stats.count('+')
        removed += stats.count('-')
    return {"lines_added": added, "lines_removed": removed, "files_changed": files_changed}
