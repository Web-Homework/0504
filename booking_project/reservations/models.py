from django.db import models
from django.contrib.auth.models import User

class TimeSlot(models.Model):
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return f"{self.start.strftime('%H:%M')} - {self.end.strftime('%H:%M')}"

class Seat(models.Model):
    row = models.IntegerField()
    col = models.IntegerField()

    class Meta:
        unique_together = ("row", "col")

    def __str__(self):
        return f"R{self.row}C{self.col}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [("booked","Booked"), ("cancelled","Cancelled")]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="booked")

    class Meta:
        unique_together = ("seat", "timeslot")

    def __str__(self):
        return f"{self.user} - {self.seat} @ {self.timeslot}"
