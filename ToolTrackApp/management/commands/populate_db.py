from django.core.management.base import BaseCommand

from ToolTrackApp.Admin.models import Admin
from ToolTrackApp.Booking.models import Booking
from ToolTrackApp.Building.models import Building
from ToolTrackApp.Faculty.models import Faculty
from ToolTrackApp.RoomWithItems.models import RoomWithItems
from ToolTrackApp.Student.models import Student
from ToolTrackApp.Item.models import Item
from ToolTrackApp.RoomToRent.models import RoomToRent


class Command(BaseCommand):

    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Student.objects.all().delete()
        Item.objects.all().delete()
        RoomToRent.objects.all().delete()
        RoomWithItems.objects.all().delete()
        Building.objects.all().delete()
        Faculty.objects.all().delete()
        Booking.objects.all().delete()
        Admin.objects.all().delete()

        # Create faculties
        faculty = Faculty.objects.create(name='Engineering Faculty')

        # Create buildings
        building1 = Building.objects.create(name='Building A', faculty=faculty)
        building2 = Building.objects.create(name='Building B', faculty=faculty)

        # Create rooms
        rooms = [
            RoomToRent(room_number=302, building=building1),
            RoomToRent(room_number=502, building=building2)
        ]
        RoomToRent.objects.bulk_create(rooms)

        # Create RoomWithItems
        room_with_items_1 = RoomWithItems.objects.create(room_number=401, building=building1)
        room_with_items_2 = RoomWithItems.objects.create(room_number=601, building=building2)

        # Create items and associate them with RoomWithItems
        items = [
            Item(name='Calculator', amount=3, room_with_items=room_with_items_2),
            Item(name='Blanket', amount=3, room_with_items=room_with_items_2),
            Item(name='Medicine', amount=3, room_with_items=room_with_items_2),
            Item(name='Earphone', amount=3, room_with_items=room_with_items_1),
            Item(name='Ruler', amount=3, room_with_items=room_with_items_1),
            Item(name='Tissue', amount=3, room_with_items=room_with_items_1)
        ]
        Item.objects.bulk_create(items)

        # Create students
        students = [
            Student(login=23019810, password='pass1', room=rooms[0]),  # Student renting Room 302
            Student(login=20019801, password='pass2', room=rooms[1])  # Student renting Room 502
        ]
        Student.objects.bulk_create(students)

        # Create admins
        admin1 = Admin.objects.create(login=101, password='adminpass1', super_admin='Y')
        admin2 = Admin.objects.create(login=102, password='adminpass2', super_admin='N')

        # Create bookings for students renting rooms
        bookings = [
            Booking(room=rooms[0], student=students[0], start_time='2024-10-01', end_time='2024-10-05'),
            Booking(room=rooms[1], student=students[1], start_time='2024-10-03', end_time='2024-10-07')
        ]
        Booking.objects.bulk_create(bookings)

        # Output a success message
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with example data'))
