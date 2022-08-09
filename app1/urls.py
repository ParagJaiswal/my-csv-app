from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('record_csv_file', views.get_csv_file, name='get_csv_file'),
]