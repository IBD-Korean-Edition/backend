from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Student(models.Model):
    login = models.IntegerField(unique=True)
    password = models.CharField(max_length=255)
    room = models.OneToOneField('RoomToRent.RoomToRent', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Student {self.login}'

    @staticmethod
    def sign_up(login, password):
        if Student.objects.filter(login=login).exists():
            return None  # Student with this login already exists
        hashed_password = make_password(password)
        student = Student.objects.create(login=login, password=hashed_password)
        return student

    @staticmethod
    def sign_in(login, password):
        try:
            student = Student.objects.get(login=login)
            if check_password(password, student.password):
                return student
            else:
                return None  # Incorrect password
        except Student.DoesNotExist:
            return None  # Student not found
