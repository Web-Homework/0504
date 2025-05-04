from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from .models import Reservation

@shared_task
def send_upcoming_reminders():
    now = timezone.now()
    in_one_hour = now + timedelta(hours=1)
    upcoming = Reservation.objects.filter(
        timeslot__start__gte=now.time(),
        timeslot__start__lt=in_one_hour.time(),
        status="booked"
    )
    for r in upcoming:
        send_mail(
            subject="座位使用提醒",
            message=f"親愛的 {r.user.username}，您預約的座位 {r.seat} 將在 {r.timeslot} 開始。",
            from_email="no-reply@example.com",
            recipient_list=[r.user.email],
        )
