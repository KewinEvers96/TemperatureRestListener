from rest_framework import viewsets
from tempListener.serializers import TemperatureSerializer
from tempListener.models import Temperature

class TemperatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint 
    """
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer


