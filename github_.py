import base64
from github import Github
from pprint import pprint
username = 'sid86-dev'

g = Github()

user = g.get_user(username)

for repo in user.get_repos():
    sp = repo.name
    print(sp)