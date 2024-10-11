from django.db import models

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_photo = models.ImageField(upload_to='car_photos/')
    available_dates = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.car_name
