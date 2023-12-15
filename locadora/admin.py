from django.contrib import admin
from .models import Car, User, Reservation

# Register your models here.

admin.site.register(Car)
admin.site.register(Reservation)
admin.site.register(User)
