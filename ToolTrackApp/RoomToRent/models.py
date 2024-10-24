from django.db import models


class RoomToRent(models.Model):
    room_number = models.IntegerField()
    building = models.ForeignKey('Building.Building', related_name='rooms', on_delete=models.CASCADE)

    def __str__(self):
        return f'Room {self.room_number} in {self.building.name}'

    def create_booking(self, student, start_date, end_date):
        # Avoid circular import by importing Booking inside the method
        from ToolTrackApp.Booking.models import Booking
        if self.is_available(start_date, end_date):
            booking = Booking.objects.create(room=self, student=student, start_time=start_date, end_time=end_date)
            return booking
        return None

    def cancel_reservation(self, booking_id):
        from ToolTrackApp.Booking.models import Booking
        try:
            booking = Booking.objects.get(id=booking_id, room=self)
            booking.delete()
            return True
        except Booking.DoesNotExist:
            return False

    def is_available(self, start_date, end_date):
        from ToolTrackApp.Booking.models import Booking
        overlapping_bookings = Booking.objects.filter(
            room=self,
            start_time__lte=end_date,
            end_time__gte=start_date
        )
        return not overlapping_bookings.exists()

    def get_all_bookings(self):
        # Using related_name if defined in Booking model, otherwise default booking_set
        return self.booking_set.all()
