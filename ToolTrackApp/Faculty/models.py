from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def add_building(self, building_name):
        # Import Building inside the method to avoid circular import
        from ToolTrackApp.Building.models import Building
        building = Building.objects.create(name=building_name, faculty=self)
        return building

    def remove_building(self, building_id):
        # Import Building inside the method to avoid circular import
        from ToolTrackApp.Building.models import Building
        try:
            building = Building.objects.get(id=building_id, faculty=self)
            building.delete()
            return True
        except Building.DoesNotExist:
            return False
