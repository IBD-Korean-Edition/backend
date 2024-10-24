from django.db import models
from django.db import models
from ToolTrackApp.RoomWithItems.models import RoomWithItems


class Item(models.Model):
    name = models.CharField(max_length=60)
    amount = models.IntegerField()
    student = models.OneToOneField('Student.Student', null=True, blank=True, on_delete=models.SET_NULL)
    room_with_items = models.ForeignKey('RoomWithItems.RoomWithItems', related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
