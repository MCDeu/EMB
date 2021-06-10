from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from django.views.generic import ListView
#from graphos.sources.modle import ModelDataSource

from .models import Data, Arduino
from .tables import DataTable
from .serializers import DataSerializer, ArduinoSerializer

# Create your views here.

class DataList(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    
class DataTable(SingleTableView):
		model = Data
		table_class = DataTable
		template_name = 'data.html'
		
class FileredDataView(SingleTableMixin, FilterView):
		table_calss = DataTable
		model = Data
		template_name = 'filter.html'
		
class ArduinoList(generics.ListCreateAPIView):
    queryset = Arduino.objects.all()
    serializer_class = ArduinoSerializer
