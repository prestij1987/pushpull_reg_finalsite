from django.db import models
from datetime import datetime

# Create your models here.


class Task(models.Model):
    given = models.DateTimeField(null=True, blank=True)
    deadline = models.DateField()
    description = models.CharField(max_length=1024)
    done = models.BooleanField(default=False)


class Dist(models.Model):
    city_pogruz = models.CharField(max_length=1024)
    city_vygruz = models.CharField(max_length=1024)
    time_way = models.DateField(datetime.now())

    def __str__(self):
        return self.city_pogruz + " -- " + self.city_vygruz + "(" + self.time_way.strftime("%Y-%B-%d") + ")"
    

