from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    holderId = models.IntegerField(default=0)
    roomId = models.IntegerField(default=302)

    def __str__(self):
        return self.name