from django.db import models

from ToolTrackApp.Building.models import Building


class RoomWithItems(models.Model):
    room_number = models.IntegerField()
    building = models.ForeignKey('Building.Building', related_name='room_with_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Room {self.room_number} in {self.building.name}'

    def add_item(self, item_name, amount):
        from ToolTrackApp.Item.models import Item
        item = Item.objects.create(name=item_name, amount=amount, room_with_items=self)
        return item

    def remove_item(self, item_id):
        try:
            from ToolTrackApp.Item.models import Item
            item = Item.objects.get(id=item_id, room_with_items=self)
            item.delete()
            return True
        except Item.DoesNotExist:
            return False

    def check_item(self, item_id):
        from ToolTrackApp.Item.models import Item
        try:
            return Item.objects.get(id=item_id, room_with_items=self)
        except Item.DoesNotExist:
            return None

    def check_all_items(self):
        return self.items.all()

    def borrow_item(self, student, item_id):
        from ToolTrackApp.Item.models import Item
        try:
            item = self.items.get(id=item_id, student__isnull=True)
            item.student = student
            item.save()
            return item
        except Item.DoesNotExist:
            return None

    def return_item(self, student):
        from ToolTrackApp.Item.models import Item
        try:
            item = Item.objects.get(student=student, room_with_items=self)
            item.student = None
            item.save()
            return True
        except Item.DoesNotExist:
            return False
