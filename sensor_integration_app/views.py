# sensor_integration_app/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

from .services import SensorIntegrationService

@csrf_exempt
@require_POST
def receive_sensor_data(request):
    data = json.loads(request.body.decode('utf-8'))
    sensor_name = data.get('name')
    sensor_type = data.get('type')
    value = data.get('value')

    if sensor_name and sensor_type and value is not None:
        SensorIntegrationService.integrate_sensor_data(sensor_name, sensor_type, value)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)
