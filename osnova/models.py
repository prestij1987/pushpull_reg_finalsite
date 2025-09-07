from django.db import models

class Event(models.Model):
    text = models.CharField(max_length = 1024)
    data = models.DateField(max_length= 100)
    itog = models.BooleanField(True)