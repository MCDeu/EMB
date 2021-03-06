from django.urls import path

from .views import DataList, DataTable, FileredDataView, ArduinoList, ArduinoListDestroy, select, demo

urlpatterns = [
    path('data/update/', DataList.as_view()),
    path('data/view/', DataTable.as_view()),
    path('data/filter/', FileredDataView.as_view()),
    path('station/update/', ArduinoList.as_view()),
    path('station/destroy/<int:pk>/', ArduinoListDestroy.as_view()),
    path('select/', select, name='select'),
    path('demo/', demo, name='demo')
]
