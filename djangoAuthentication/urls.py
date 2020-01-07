"""djangoAuthentication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from authView import views
from django.contrib.auth import views as auth_views
from . import views as vviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authView.urls', namespace='authView')),
    # path('', include('authView.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', vviews.HomePage.as_view(), name='home'),
    path('test/', vviews.TestPage.as_view(), name='test'),
    path('thanks/', vviews.ThanksPage.as_view(), name='thanks'),

    path("login/", auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUp.as_view(template_name="signup.html"), name="signup"),
]
