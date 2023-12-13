# sensor_integration_app/services.py

from .models import Sensor, SensorData

class SensorIntegrationService:
    @staticmethod
    def integrate_sensor_data(sensor_name, sensor_type, value):
        sensor, created = Sensor.objects.get_or_create(name=sensor_name, sensor_type=sensor_type)
        SensorData.objects.create(sensor=sensor, value=value)

