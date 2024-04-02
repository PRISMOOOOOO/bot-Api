from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Weather(models.Model):
    temperatrue = models.CharField(max_length=255)
    humidity = models.CharField(max_length=255)
    weather = models.CharField(max_length=255)
    wind_speed = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    create_as = models.DateTimeField(auto_now_add = True)
    update_as = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.location+" | " + str(self.create_as)
