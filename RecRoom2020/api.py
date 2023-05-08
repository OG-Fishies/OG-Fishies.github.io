
#this was a test




import requests

API = requests.get('https://ogfishiesyt.github.io/RR2020.github.io/CommunityBoard.json')

#CurrentAnnouncement
Announcement = API.json()['CurrentAnnouncement']['Message']
MoreInfoUrl = API.json()['CurrentAnnouncement']['MoreInfoUrl']
#videos
video1 = API.json()['Videos'][0]['BlobName']
video2 = API.json()['Videos'][1]['BlobName']
video3 = API.json()['Videos'][2]['BlobName']
#Titles
Title1 = API.json()['Videos'][0]['Title']
Title2 = API.json()['Videos'][1]['Title']
Title3 = API.json()['Videos'][2]['Title']
#testing
print(Announcement)
print(MoreInfoUrl)
print()
print(video1)
print(Title1)
print()
print(video2)
print(Title2)
print()
print(video3)
print(Title3)