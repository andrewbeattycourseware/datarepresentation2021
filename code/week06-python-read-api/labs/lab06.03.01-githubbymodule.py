# to use this install package
# pip install PyGithub
from github import Github
import requests


# THIS key will not work for you,
# you will have to get your own key from github and use that 
g = Github("XXXXXXX7aa146eafee094d3a7b1e81aa1d8fcb0eec8b910XXXXXXXXX")

#for repo in g.get_user().get_repos():
#    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
# make sure this replository exists, and that the path is correct
repo = g.get_repo("YOUR-USER-NAME/aPrivateOneXXXXXX")
#print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)
newContents = contentOfFile + " more stuff \n"
print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)
