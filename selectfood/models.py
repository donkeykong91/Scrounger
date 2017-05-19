from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=20)

class Event(models.Model):
    event_date_time = models.DateTimeField()
    event_location = models.CharField(max_length=20)
