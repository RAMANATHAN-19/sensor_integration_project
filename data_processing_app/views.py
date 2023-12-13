# data_processing_app/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

from .services import DataProcessingService
from sensor_integration_app.models import SensorData

@csrf_exempt
@require_POST
def process_sensor_data(request):
    data = json.loads(request.body.decode('utf-8'))
    sensor_data_id = data.get('sensor_data_id')

    if sensor_data_id is not None:
        try:
            sensor_data = SensorData.objects.get(id=sensor_data_id)
            DataProcessingService.process_sensor_data(sensor_data)
            return JsonResponse({'status': 'success'})
        except SensorData.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Sensor data not found'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)

