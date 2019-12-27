from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from authView import views

app_name = 'authView'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('help/', views.help, name = 'help'),
    path('about/', views.about, name = 'about'),
    url("login/", auth_views.LoginView.as_view(template_name="authView/login.html"),name='login'),
    url("logout/", auth_views.LogoutView.as_view(), name="logout"),
    url("signup/", views.SignUp.as_view(), name="signup"),


]
#djangoAuthentication\templates\authView\login.html djangoAuthentication/templates/authView/
