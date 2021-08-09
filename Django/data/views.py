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
from .utils import *
from .GenerateKML import *
from .ManageData import *
from .ConfigurationFile import *

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

class ArduinoListDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Arduino.objects.all()
    serializer_class = ArduinoSerializer

def select(request):
    LoadConfigFile()
    if request.method == 'POST':
        if request.POST.get("Submit") == "Submit":
            run_select(request)
        if request.POST.get("Stop") == "Stop":
            stop_thread()

    return render(request, 'select.html', {})

def run_select(request):
    id_station=request.POST.get('Id_Station')
    day=request.POST.get('Day')
    hour=request.POST.get('Hour')
    minute=request.POST.get('Minute')
    
    date = GetDate(day,hour,minute)
    coordinades = GetCoordinatesFromId(id_station)
    data = GetDataFromId(id_station,date)
    
    CreateKML(data, coordinades)
    
    #sendKmlToLGCommon(global_vars.kml_destination_filename)
    #flyToRegion(region)
