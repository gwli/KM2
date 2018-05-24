# -*- coding: utf-8 -*-

# Uses Python 2.7
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import json

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
#USERNAME = os.environ['GITHUB_USER']
#TOKEN = os.environ['GITHUB_TOKEN']

USERNAME = "gwli"
TOKEN = "6a6d7aefb691f44f0d6d9926a219d5d67658d592"
# The repository to add this issue to
REPO_OWNER = USERNAME
REPO_NAME = 'DeepLearningOnGPU'

def make_github_issue(title, body=None, created_at=None, closed_at=None, updated_at=None, assignee=None, milestone=None, closed=None, labels=None):
    # Create an issue on github.com using the given parameters
    # Url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/import/issues' % (REPO_OWNER, REPO_NAME)
    
    # Headers
    headers = {
        "Authorization": "token %s" % TOKEN,
        "Accept": "application/vnd.github.golden-comet-preview+json"
    }
    
    # Create our issue
    data = {'issue': {'title': title,
                      'body': body,
                      'assignee': assignee,
                      'milestone': milestone,
                      'closed': closed,
                      'labels': labels}}

    payload = json.dumps(data)

    # Add the issue to our repository
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 202:
        print 'Successfully created Issue "%s"' % title
    else:
        print 'Could not create Issue "%s"' % title
        print 'Response:', response.content


title = 'Pretty title'
body = 'Beautiful body'
created_at = "2014-01-01T12:34:58Z"
closed_at = "2014-01-02T12:24:56Z"
updated_at = "2014-01-03T11:34:53Z"
assignee = 'username'
milestone = 1
closed = False
labels = [
    "bug", "low", "energy"
]

make_github_issue(title, body, created_at, closed_at, updated_at, assignee, milestone, closed, labels)
#make_github_issue(title, body,)
