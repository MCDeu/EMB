from django.urls import path

from .views import DataList, DataTable, FileredDataView

urlpatterns = [
    path('updatedades/', DataList.as_view()),
    path('viewdades/', DataTable.as_view()),
    path('filterdades/', FileredDataView.as_view()),
]
