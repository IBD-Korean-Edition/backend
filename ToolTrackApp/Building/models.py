from django.db import models

from ToolTrackApp.RoomToRent.models import RoomToRent


class Building(models.Model):
    name = models.CharField(max_length=10)
    faculty = models.ForeignKey('Faculty.Faculty', related_name='buildings', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def add_room_to_rent(self, room_number):
        room = RoomToRent.objects.create(room_number=room_number, building=self)
        return room

    def add_room_with_items(self, room_number):
        from ToolTrackApp.RoomWithItems.models import RoomWithItems
        room_with_items = RoomWithItems.objects.create(room_number=room_number, building=self)
        return room_with_items

    def check_all_rooms_to_rent(self):
        return self.rooms.all()

    def check_all_rooms_with_items(self):
        return self.room_with_items.all()
