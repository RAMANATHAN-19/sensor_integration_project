# sensor_integration_app/models.py

from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=255)
    sensor_type = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name  # Display the sensor name in the admin

class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    def __str__(self):
        return f"{self.sensor.name} - {self.timestamp}"  # Display sensor name and timestamp in the admin

