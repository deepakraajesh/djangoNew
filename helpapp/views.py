from django.shortcuts import render
from django.http import HttpResponse
from helpapp.models import *
from . import forms

def index(request):
    return HttpResponse("Worked")

def help(request):
    web_list=AccessRecord.objects.order_by('date')
    date_dict={'access_record':web_list}

    """helpd will not be used now, as we are passing date_dict in the context"""
    helpd = {'help_page':"You're viewing helpd value."}

    return render(request,'helpapp/help.html',context=date_dict)

def form_name_view(request):
    form = forms.FormName()
    return render(request,'helpapp/forms.html',{'form':form})
