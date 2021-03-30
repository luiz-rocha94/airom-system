from django.db import models


class HeartFailure(models.Model):
    age = models.IntegerField()
    anaemia = models.BinaryField()
    creatinine_phosphokinase = models.FloatField()
    diabetes = models.BinaryField()
    ejection_fraction = models.FloatField()
    high_blood_pressure = models.BinaryField()
    platelets = models.FloatField()
    serum_creatinine = models.FloatField()
    serum_sodium = models.FloatField()
    sex = models.BinaryField()
    smoking = models.BinaryField()
    time = models.IntegerField()
    death_event = models.BinaryField()
