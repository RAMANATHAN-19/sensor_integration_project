# data_processing_app/admin.py

from django.contrib import admin
from .models import ProcessedSensorData

class ProcessedSensorDataAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'timestamp', 'processed_value')

admin.site.register(ProcessedSensorData, ProcessedSensorDataAdmin)

