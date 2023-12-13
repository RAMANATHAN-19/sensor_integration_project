# data_processing_app/services.py

from .models import ProcessedSensorData
from sensor_integration_app.models import SensorData

class DataProcessingService:
    @staticmethod
    def process_sensor_data(sensor_data):
        # Implement your data processing logic based on sensor type
        # Example: Double the value for demonstration purposes
        processed_value = 2 * sensor_data.value

        # Save processed data
        ProcessedSensorData.objects.create(
            sensor_name=sensor_data.sensor.name,
            timestamp=sensor_data.timestamp,
            processed_value=processed_value
        )

