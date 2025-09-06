from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bookings")
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.event.name}"

