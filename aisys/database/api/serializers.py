from rest_framework import serializers
from .. import models


class HeartFailureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeartFailure
        fields = '__all__'
