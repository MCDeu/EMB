from time import sleep, time
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
            stopOrbit()
            resetView()

    return render(request, 'select.html', {})
    
def run_select(request):
    id_station=request.POST.get('Id_Station')
    day=request.POST.get('Day')
    hour=request.POST.get('Hour')
    minute=request.POST.get('Minute')
    
    date = GetDate(day,hour,minute)
    coordinates = GetCoordinatesFromId(id_station)
    regions = coordinates.split()
    data = GetDataFromId(id_station,date)
    
    CreateKML(data, coordinates)
    
    sendKmlToLGCommon(global_vars.kml_destination_filename)
    flyToRegion(regions, 1440)
    
def demo(request):
    LoadConfigFile()
    if request.method == 'POST':
        print("Metod post")
        if request.POST.get("Submit") == "Submit":
            print("run_demo starts")
            run_demo(request)
        if request.POST.get("Stop") == "Stop":
            stop_thread()

    return render(request, 'demo.html', {})

def run_demo(request):
    id_station=['01000001', '01001001', '01011000', '01000000', '00100001', '00100011', '01010111', '01100000', '01100001']
    
    date = "2021-05-01 00:00:00"
    
    for x in id_station:
        coordinates = GetCoordinatesFromId(x)
        regions = coordinates.split()
        data = GetDataFromId(x,date)
    
        CreateKML(data, coordinates)
        sendKmlToLGCommon(global_vars.kml_destination_filename)
        flyToRegion(regions, 360)
        sleep(18.2)
