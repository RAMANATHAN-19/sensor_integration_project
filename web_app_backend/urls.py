# web_app_backend/urls.py

from django.urls import path
from .views import get_sensor_data, get_processed_data

urlpatterns = [
    path('get_sensor_data/', get_sensor_data, name='get_sensor_data'),
    path('get_processed_data/', get_processed_data, name='get_processed_data'),
]

