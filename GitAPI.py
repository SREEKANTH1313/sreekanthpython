import requests
from pprint import pprint
import base64
from github import Github
from pprint import pprint


User_input = input("Enter the github username:")

g = Github()
user = g.get_user(User_input)

for repo in user.get_repos():
    print(repo)

request = requests.get('https://api.github.com/users/' + User_input + '/repos')
json = request.json()
for i in range(0, len(json)):
  print("Project Number:", i+1)
  print("Project Name:", json[i]['name'])
  print("Project URL:", json[i]['svn_url'], "\n")

#Output

# Enter the github username:SREEKANTH1313
# Repository(full_name="SREEKANTH1313/1313")
# Repository(full_name="SREEKANTH1313/Gitfiles")
# Repository(full_name="SREEKANTH1313/gith")
# Repository(full_name="SREEKANTH1313/gitignore-test")
# Repository(full_name="SREEKANTH1313/git_files")
# Repository(full_name="SREEKANTH1313/hello-git")
# Repository(full_name="SREEKANTH1313/hiisree")
# Repository(full_name="SREEKANTH1313/merge_conflicts")
# Repository(full_name="SREEKANTH1313/pull-request-demo")
# Repository(full_name="SREEKANTH1313/python-")
# Repository(full_name="SREEKANTH1313/Revert")
# Repository(full_name="SREEKANTH1313/sree")
# Repository(full_name="SREEKANTH1313/SREE1")
# Repository(full_name="SREEKANTH1313/sreekanthpython")
# Project Number: 1
# Project Name: 1313
# Project URL: https://github.com/SREEKANTH1313/1313 

# Project Number: 2
# Project Name: Gitfiles
# Project URL: https://github.com/SREEKANTH1313/Gitfiles 

# Project Number: 3
# Project Name: gith
# Project URL: https://github.com/SREEKANTH1313/gith 

# Project Number: 4
# Project Name: gitignore-test
# Project URL: https://github.com/SREEKANTH1313/gitignore-test 

# Project Number: 5
# Project Name: git_files
# Project URL: https://github.com/SREEKANTH1313/git_files 

# Project Number: 6
# Project Name: hello-git
# Project URL: https://github.com/SREEKANTH1313/hello-git 

# Project Number: 7
# Project Name: hiisree
# Project URL: https://github.com/SREEKANTH1313/hiisree 

# Project Number: 8
# Project Name: merge_conflicts
# Project URL: https://github.com/SREEKANTH1313/merge_conflicts 

# Project Number: 9
# Project Name: pull-request-demo
# Project URL: https://github.com/SREEKANTH1313/pull-request-demo 

# Project Number: 10
# Project Name: python-
# Project URL: https://github.com/SREEKANTH1313/python- 

# Project Number: 11
# Project Name: Revert
# Project URL: https://github.com/SREEKANTH1313/Revert 

# Project Number: 12
# Project Name: sree
# Project URL: https://github.com/SREEKANTH1313/sree 

# Project Number: 13
# Project Name: SREE1
# Project URL: https://github.com/SREEKANTH1313/SREE1 

# Project Number: 14
# Project Name: sreekanthpython
# Project URL: https://github.com/SREEKANTH1313/sreekanthpython 


# Process finished with exit code 0
