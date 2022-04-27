from email.policy import default
from tempListener.models import Temperature
from rest_framework import serializers
from django.utils import timezone

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    
    registeredTime = serializers.DateTimeField(required = False, default = timezone.now())

    class Meta:
        model = Temperature
        fields = ['url','id', 'temp', 'registeredTime']




