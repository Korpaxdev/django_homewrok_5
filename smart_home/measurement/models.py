from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    photo = models.ImageField(upload_to='measurements/%Y/%m/%d', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sensor.name}: {self.temperature}'
