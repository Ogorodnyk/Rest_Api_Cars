from django.contrib import admin

# Register your models here.

from .models import Car, CarRate, GiveRate

admin.site.register(Car)
admin.site.register(CarRate)
admin.site.register(GiveRate)