from django.db import models
from django.utils import timezone

class Food(models.Model):
    food_name = models.CharField(max_length=20)
    def __str__(self):
        return self.food_name

class Event(models.Model):
    event_date_time = models.DateTimeField()
    event_location = models.CharField(max_length=20)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    def __str__(self):
        return self.event_location
