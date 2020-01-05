from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from authView import views

app_name = 'authView'

urlpatterns = [

    path('help/', views.help, name = 'help'),
    path("about/", views.AboutPage.as_view(template_name="about.html"), name = 'about'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUp.as_view(template_name="signup.html"), name="signup"),


]
#djangoAuthentication\templates\authView\login.html djangoAuthentication/templates/authView/
