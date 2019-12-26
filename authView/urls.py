from django.conf.urls import url
from django.urls import path
from authView import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('help/', views.help, name = 'help'),
    path('about/', views.about, name = 'about'),


]
