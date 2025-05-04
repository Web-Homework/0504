from django.urls import path
from .views import dashboard, reserve_time, my_records, seat_map_api

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("slot/<int:slot_id>/", reserve_time, name="reserve_time"),
    path("my-records/", my_records, name="my_records"),
    path("api/seats/<int:slot_id>/", seat_map_api, name="seat_map_api"),
]
