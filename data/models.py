from django.db import models
from datetime import datetime

# Create your models here.

class Data(models.Model):
    ID_Arduino = models.CharField(max_length=8)
    dia = models.DateTimeField(default=datetime.now)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    temperatura = models.CharField(max_length=50)
    pressio = models.CharField(max_length=50)
    pluja = models.CharField(max_length=50)
    humitat_aire = models.CharField(max_length=50)
    humitat_terrestre = models.CharField(max_length=50)
    velocitat_vent = models.CharField(max_length=50)
    direccio_vent = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dia
