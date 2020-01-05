from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView

from . import forms
from django.contrib.auth import login, logout
# Create your views here.


def help(request):
    helpDict = {'insertHelp' : 'This is from help views'}
    return render(request, 'help.html', context = helpDict)

class AboutPage(TemplateView):
    template_name = 'about.html'


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
