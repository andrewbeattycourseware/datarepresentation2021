import requests
import json

# get your own API key for github
apiKey = 'XXX7aa146eafee094d3a7b1e81aa1d8fcb0eec8b910XXX'
url = 'https://api.github.com/repos/your-username/aprivateone'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)

