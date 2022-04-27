from xml.dom.domreg import registered
from django.db import models

# Create your models here.

class Temperature(models.Model):
    temp = models.DecimalField( max_digits= 4, decimal_places=2)
    registeredTime = models.DateTimeField()


