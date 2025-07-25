#!/usr/bin/python3
"""
Script that lists 10 commits (from most recent to oldest) of a repository
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repo_name)
    
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        
        # Get the first 10 commits (most recent)
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print("{}: {}".format(sha, author_name))
