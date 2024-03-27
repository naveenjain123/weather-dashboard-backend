"""weather history model"""
from django.utils import timezone
from django.db import models


class WeatherHistory(models.Model):
    """weather history model"""

    country = models.CharField(max_length=1000)
    temp = models.IntegerField(null=False, default=0)
    feels_like = models.IntegerField(null=False, default=0)
    temp_min = models.IntegerField(null=False, default=0)
    temp_max = models.IntegerField(null=False, default=0)
    pressure = models.IntegerField(null=False, default=0)
    sea_level = models.IntegerField(null=False, default=0)
    grnd_level = models.IntegerField(null=False, default=0)
    humidity = models.IntegerField(null=False, default=0)
    temp_kf = models.IntegerField(null=False, default=0)
    timestamp = models.DateTimeField(null=False, default=timezone.now())

    class Meta:
        verbose_name = "weather history"
        verbose_name_plural = "weather history"
        db_table = "weather_history"

    def __str__(self):
        return self.country
