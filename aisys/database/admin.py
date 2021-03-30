from django.contrib import admin
from . import models


class HeartFailureAdmin(admin.ModelAdmin):
    list_display = ('id', 'age', 'anaemia', 'creatinine_phosphokinase',
                    'diabetes', 'ejection_fraction', 'high_blood_pressure',
                    'platelets', 'serum_creatinine', 'serum_sodium', 'sex',
                    'smoking', 'time', 'death_event')


admin.site.register(models.HeartFailure, HeartFailureAdmin)
