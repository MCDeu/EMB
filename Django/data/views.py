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

class ArduinoListDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Arduino.objects.all()
    serializer_class = ArduinoSerializer

def present(request):
    LoadConfigFile()
    if request.method == 'POST':
        if request.POST.get("Submit") == "Submit":
            cleanVerbose()
            writeVerbose('Expect several minutes to complete...')
            run_present(request)
        if request.POST.get("Stop") == "Stop":
            stop_thread()

    return render(request, 'present.html', {})

def run_present(request):
    region = GetRegionFromFile(request.POST.get('region'))
    GenerateRealTimeKML(region)
    sendKmlToLGCommon(global_vars.kml_destination_filename)
    flyToRegion(region)