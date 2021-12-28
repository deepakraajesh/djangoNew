from django.shortcuts import render

def index(request):
    dictd = {'text':'hello world!!..'}
    return render(request,'basicapp/index.html',context={'form':dictd})

def basicapp(request):
    return render(request,'basicapp/base.html')

def relative(request):
    return render(request,'basicapp/relative_url_templates.html')
