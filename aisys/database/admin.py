from django.contrib import admin
from . import models


class UsedCarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'year', 'price', 'transmission', 'mileage', 'fueltype',
                    'tax', 'mpg', 'enginesize')


admin.site.register(models.UsedCar, UsedCarAdmin)
