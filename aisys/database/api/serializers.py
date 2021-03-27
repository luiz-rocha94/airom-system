from rest_framework import serializers
from .. import models


class UsedCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsedCar
        fields = '__all__'
