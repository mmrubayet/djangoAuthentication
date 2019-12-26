from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")

    dict = {'insert_me':'Hello, This is from views.py file !'}
    return render(request, 'authView/index.html', context = dict)


def help(request):

    helpDict = {'insertHelp' : 'This is from help views'}
    return render(request, 'authView/help.html', context = helpDict)

def about(request):
    return render(request, 'authView/about.html',)
