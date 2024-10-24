from django.db import models
from ToolTrackApp.Borrow.models import Item

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=302)
    
    # name : rooms connect Item model and Room models
    items = models.ManyToManyField(Item, related_name='rooms')

    def __str__(self):
        return self.name