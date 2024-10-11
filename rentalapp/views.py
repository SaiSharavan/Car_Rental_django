from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
def register(request):
    from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Car

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check if email or username already exists
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Exist')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('register')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully. You can now login.")
        return redirect('login')

    return render(request, 'register.html')




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

         
def logout(request):
    auth.logout(request)
    return redirect('/')
   
def upload_car(request):
    if request.method == 'POST':
        car_name = request.POST.get('car_name')
        available_dates = request.POST.get('available_dates')
        price = request.POST.get('price')
        car_photo = request.FILES['car_photo']

        car = Car(
            car_name=car_name,
            available_dates=available_dates,
            price=price,
            car_photo=car_photo
        )
        car.save()

        return redirect('cars')  # Redirect to the page that lists the cars
    return render(request, 'upload_car.html')    
