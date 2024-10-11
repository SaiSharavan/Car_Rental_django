from django.contrib import admin
from .models import Car,Booking  # Import your Car model

# Register the Car model
admin.site.register(Car)
admin.site.register(Booking)
