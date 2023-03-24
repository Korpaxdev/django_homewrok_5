from django.urls import path
from .views import *

urlpatterns = [
    path('sensors/', SensorsView.as_view(), name='sensors'),
    path('sensors/<pk>', SensorDetailView.as_view(), name='sensor_detail'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement'),
    # TODO: зарегистрируйте необходимые маршруты
]
