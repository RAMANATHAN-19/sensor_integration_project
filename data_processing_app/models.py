# data_processing_app/models.py

from django.db import models

class ProcessedSensorData(models.Model):
    sensor_name = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    processed_value = models.FloatField()

    def __str__(self):
        return f"{self.sensor_name} - {self.timestamp} - {self.processed_value}"

