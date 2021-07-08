from django.db import models
from datetime import datetime

# Create your models here.


class Arduino(models.Model):
    id_station = models.CharField(max_length=8, primary_key=True)
    model_arduino = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lon = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)

class Data(models.Model):
    id_station = models.ForeignKey('Arduino', on_delete=models.CASCADE)
    day = models.DateTimeField(default=datetime.now)
    temperature = models.CharField(max_length=50)
    press = models.CharField(max_length=50)
    rain = models.CharField(max_length=50)
    air_humidity = models.CharField(max_length=50)
    wind_speed = models.CharField(max_length=50)
    wind_direction = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dia

