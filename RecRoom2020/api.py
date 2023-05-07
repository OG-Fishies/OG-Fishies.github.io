import requests

API = requests.get('https://ogfishiesyt.github.io/RR2020.github.io/CommunityBoard.json')

#videos
video1 = API.json()['Videos'][0]['BlobName']
video2 = API.json()['Videos'][1]['BlobName']
video3 = API.json()['Videos'][2]['BlobName']
#Titles
Title1 = API.json()['Videos'][0]['Title']
Title2 = API.json()['Videos'][1]['Title']
Title3 = API.json()['Videos'][2]['Title']