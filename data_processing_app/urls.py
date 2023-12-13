# data_processing_app/urls.py

from django.urls import path
from .views import process_sensor_data

urlpatterns = [
    path('process_sensor_data/', process_sensor_data, name='process_sensor_data'),
]


