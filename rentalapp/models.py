from django.db import models

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_photo = models.ImageField(upload_to='D/')
    available_dates = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.car_name

# car/models.py

from django.utils import timezone  # Import timezone for current time

class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    booking_time = models.DateTimeField(default=timezone.now)  # Provide a default value

    def __str__(self):
        return f"{self.user_name} - {self.car_name} - ${self.price} - {self.booking_time.strftime('%Y-%m-%d %H:%M:%S')}"
