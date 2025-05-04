import json
from channels.db import database_sync_to_async

from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Reservation, Seat, TimeSlot
from django.contrib.auth.models import AnonymousUser

class SeatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.slot_id = self.scope["url_route"]["kwargs"]["slot_id"]
        self.group_name = f"slot_{self.slot_id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")
        seat_id = data.get("seat_id")
        user = self.scope["user"]
        if user.is_anonymous:
            return

        if action == "reserve":
            # 建立或更新 reservation
            await database_sync_to_async(Reservation.objects.get_or_create)(
                user=user, seat_id=seat_id, timeslot_id=self.slot_id
            )
        elif action == "release":
            await database_sync_to_async(
                Reservation.objects.filter(
                    user=user, seat_id=seat_id, timeslot_id=self.slot_id
                ).update
            )(status="cancelled")

        # Broadcast 最新狀態
        booked = await database_sync_to_async(
            lambda: list(
                Reservation.objects
                .filter(timeslot_id=self.slot_id, status="booked")
                .values_list("seat_id", flat=True)
            )
        )()
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "seat_update",
                "booked": booked,
            }
        )

    async def seat_update(self, event):
        await self.send(text_data=json.dumps({
            "booked": event["booked"]
        }))
