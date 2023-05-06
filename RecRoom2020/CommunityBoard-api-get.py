import requests

api = requests.get("https://ogfishiesyt.github.io/RR2020.github.io/CommunityBoard.json")

rec_net = ('https://cdn.rec.net/video/')

no = int(input('no. of video'))
print (no)

BlobName0 = api.json()['Videos'][no]['BlobName']
Title0 = api.json()['Videos'][no]["Title"]



print(rec_net+BlobName0)
print(Title0)

