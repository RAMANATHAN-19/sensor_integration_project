# sensor_integration_app/admin.py

from django.contrib import admin
from .models import Sensor, SensorData

class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'sensor_type', 'status')

class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'timestamp', 'value')

admin.site.register(Sensor, SensorAdmin)
admin.site.register(SensorData, SensorDataAdmin)


