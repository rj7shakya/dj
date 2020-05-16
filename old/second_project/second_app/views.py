from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def help(request):
    mdict = {'insert_me':"help youuu "}
    return render(request,'second_app/help.html',context=mdict)

def index(request):
    return HttpResponse("hello")