from django.contrib import admin
from django.urls import path,include
from  scanhosts import views

urlpatterns = [
    path('hostscan/', views.hostscan,name='hostscan'),
    path('', views.hostscan, name='hostscan'),
]
