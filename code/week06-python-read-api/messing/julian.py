import requests
import json
#lab06.02.08 question 8
apiKey = "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"
url = "https://api.github.com/repos/juliandunne1234/aprivateone"
filename = "repo.json"

response = requests.get(url, auth=('token', apiKey))
print (response)
print (response.text)
print('\n\n')
repoJSON = response.json()



file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)
