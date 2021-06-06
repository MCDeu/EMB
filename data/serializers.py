from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('ID_Arduino', 'dia', 'latitud', 'longitud', 'temperatura', 'pressio', 'pluja',  'humitat_aire', 'humitat_terrestre', 'velocitat_vent', 'direccio_vent')
        model = Data
