# sensor_integration/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensor/', include('sensor_integration_app.urls')),
    path('data_processing/', include('data_processing_app.urls')),
    path('web_app_backend/', include('web_app_backend.urls')),
]



