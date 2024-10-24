from django.db import models

from ToolTrackApp.Student.models import Student


class Admin(models.Model):
    password = models.CharField(max_length=255)
    login = models.IntegerField(unique=True)
    super_admin = models.CharField(max_length=1)

    def __str__(self):
        return f'Admin {self.login}'

    def access_all_tables(self):
        from django.apps import apps
        all_data = {}
        models = apps.get_models()
        for model in models:
            all_data[model.__name__] = model.objects.all()
        return all_data

    def get_all_students_renting(self):
        return Student.objects.filter(room__isnull=False)
