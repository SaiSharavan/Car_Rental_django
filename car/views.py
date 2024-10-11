from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from rentalapp.models import Car,Booking
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'index.html')

def cars(request):
    cars_list = Car.objects.all()  
    return render(request, 'cars.html', {'cars': cars_list})  

def booknow(request, car_id):
    car = get_object_or_404(Car, id=car_id)  

    if request.method == 'POST':
        user_name = request.POST['user_name']

        booking = Booking(user_name=user_name, car_name=car.car_name, price=car.price)
        booking.save()

        success_message = "Booking successful!"

        return render(request, 'booknow.html', {'car': car, 'success_message': success_message})

    return render(request, 'booknow.html', {'car': car})