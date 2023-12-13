# web_app_backend/views.py

from django.http import JsonResponse
from data_processing_app.models import ProcessedSensorData
from sensor_integration_app.models import SensorData

def get_sensor_data(request):
    # Implement logic to retrieve sensor data
    sensor_data = SensorData.objects.all()  # Replace this with your actual logic
    data = [{'timestamp': entry.timestamp, 'value': entry.value} for entry in sensor_data]
    return JsonResponse({'sensor_data': data})

def get_processed_data(request):
    # Implement logic to retrieve processed data
    processed_data = ProcessedSensorData.objects.all()  # Replace this with your actual logic
    data = [{'timestamp': entry.timestamp, 'processed_value': entry.processed_value} for entry in processed_data]
    return JsonResponse({'processed_data': data})

