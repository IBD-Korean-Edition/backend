from django.db import models


class Booking(models.Model):
    room = models.ForeignKey('RoomToRent.RoomToRent', on_delete=models.CASCADE)
    student = models.ForeignKey('Student.Student', on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self):
        return f'Booking by {self.student.login} for Room {self.room.room_number}'
