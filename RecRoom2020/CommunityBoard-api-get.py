
#The API is not being ues rn



from django.http import HttpResponse
from django.shortcuts import render 

import requests

api = requests.get("https://ogfishiesyt.github.io/RR2020.github.io/CommunityBoard.json")

rec_net = ('https://cdn.rec.net/video/')

BlobName0 = api.json()['Videos'][0]['BlobName']
Title1 = api.json()['Videos'][0]["Title"]

def video1(requset):
    return render(requests, "index.html",{"q": rec_net+BlobName0})

