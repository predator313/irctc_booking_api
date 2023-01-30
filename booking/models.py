from django.db import models

# Create your models here.

class Train(models.Model):
    name = models.CharField(max_length=100)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    seats = models.PositiveSmallIntegerField()

class Ticket(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    seats = models.PositiveSmallIntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

