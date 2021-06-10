from rest_framework import serializers
from .models import Data, Arduino


class ArduinoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id_station', 'model_arduino', 'lat', 'lon', 'country', 'region', 'owner')
        model = Arduino


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id_station', 'day', 'temperature', 'press', 'rain',  'air_humidity', 'wind_speed', 'wind_direction')
        model = Data
