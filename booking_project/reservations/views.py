from django.shortcuts import render, get_object_or_404, redirect
from .models import TimeSlot, Seat, Reservation
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def dashboard(request):
    slots = TimeSlot.objects.all()
    return render(request, "reservations/dashboard.html", {"slots": slots})

@login_required
def reserve_time(request, slot_id):
    slot = get_object_or_404(TimeSlot, id=slot_id)
    seats = Seat.objects.all()
    return render(request, "reservations/reserve_time.html", {
        "slot": slot,
        "seats": seats,
    })

@login_required
def my_records(request):
    recs = Reservation.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "reservations/my_records.html", {"recs": recs})

# （如果想用 HTTP API 初始化座位狀態，可加這個 view）
@login_required
def seat_map_api(request, slot_id):
    booked = Reservation.objects.filter(timeslot_id=slot_id, status="booked")
    data = {r.seat_id: r.user_id for r in booked}
    return JsonResponse(data)
