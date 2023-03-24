from rest_framework import serializers

from measurement.models import Measurement, Sensor


# TODO: опишите необходимые сериализаторы

class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description')


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('sensor', 'temperature', 'photo', 'created_at')
        extra_kwargs = {'sensor': {'write_only': True}}


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description', 'measurements')
