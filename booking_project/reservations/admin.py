from django.contrib import admin
from .models import Seat, TimeSlot, Reservation

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("id", "row", "col")

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ("id", "start", "end")

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("user", "seat", "timeslot", "status", "created_at")


