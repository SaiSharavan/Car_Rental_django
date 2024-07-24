from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def cars(request):
    return render(request, 'cars.html') 

def booknow(request):
    return render(request,'booknow.html')