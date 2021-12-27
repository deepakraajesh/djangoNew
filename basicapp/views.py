from django.shortcuts import render

def index(request):
    return render(request,'basicapp/index.html')

def basicapp(request):
    return render(request,'basicapp/base.html')

def relative(request):
    return render(request,'basicapp/relative_url_templates.html')
