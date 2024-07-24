from django.contrib import admin
from django.urls import include, path
from car import views
#place to add urls
urlpatterns = [

    path('', views.home, name='home'),
    path('car/',views.car,name='car'),
]