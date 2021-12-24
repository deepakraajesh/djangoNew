from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Worked")

def help(request):
    helpd = {'help_page':"You're viewing helpd value."}
    return render(request,'helpapp/help.html',context=helpd)
