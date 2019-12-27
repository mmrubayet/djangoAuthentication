from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

def index(request):
    # return HttpResponse("Hello World!")

    dict = {'insert_me':'Hello, This is from views.py file !'}
    return render(request, 'authView/index.html', context = dict)
