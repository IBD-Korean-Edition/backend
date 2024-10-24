from django.db import models

# models according to swagger

class Student(models.Model):
    studentId = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)