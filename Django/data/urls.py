from django.urls import path

from .views import DataList, DataTable, FileredDataView, ArduinoList, ArduinoListDestroy

urlpatterns = [
    path('dades/update/', DataList.as_view()),
    path('dades/view/', DataTable.as_view()),
    path('dades/filter/', FileredDataView.as_view()),
    path('station/update/', ArduinoList.as_view()),
    path('station/destroy/<int:pk>/', ArduinoListDestroy.as_view()),
]
