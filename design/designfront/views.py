from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def home(request):
    return render(request, 'pages/index.html',)

def index2(request):
    return render(request, 'pages/index2.html',)


def senddata(request):
    postdata = json.loads(request.body.decode('utf-8'))
    name = postdata["name"]
    username = postdata["username"]
    password = postdata["password"]
    repassword = postdata["repassword"]
    phone = postdata["phone"]
    email = postdata["email"]
    compt = 1 
    while compt < 10000000:
        compt += 1
    issuccess = False
    if username is not None: 
        issuccess=True
    else: 
        issuccess = False
    
    
    # name = postdata['name']
    datas = {
        'succes':issuccess,
        'name':name,
    }
    return JsonResponse(datas, safe=False)