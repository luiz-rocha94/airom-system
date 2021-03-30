from django.db import models


class HeartFailure(models.Model):
    age = models.IntegerField()
    anaemia = models.IntegerField()
    creatinine_phosphokinase = models.FloatField()
    diabetes = models.IntegerField()
    ejection_fraction = models.FloatField()
    high_blood_pressure = models.IntegerField()
    platelets = models.FloatField()
    serum_creatinine = models.FloatField()
    serum_sodium = models.FloatField()
    sex = models.IntegerField()
    smoking = models.IntegerField()
    time = models.IntegerField()
    death_event = models.IntegerField()
