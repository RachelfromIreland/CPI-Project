from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.
TIME_SLOTS = [
    ('10:00', '10:00 AM - 12:00 PM'),
    ('14:00', '2:00 PM - 4:00 PM'),
]

class Booking(models.Model):
# create model for user later, test Booking first    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_name = models.CharField(max_length=100)
    num_attending = models.PositiveIntegerField()
    date = models.DateField()
    time_slot = models.CharField(max_length=5, choices=TIME_SLOTS)
    booking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date', 'time_slot')

    def __str__(self):
#        return f'{self.customer.username} - {self.booking_name} - {self.date} - {self.time_slot}'
        return f'{self.booking_name} - {self.date} - {self.time_slot}'