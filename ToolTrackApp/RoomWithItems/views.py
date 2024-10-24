from django.shortcuts import render, get_object_or_404
from .models import Room

def room_detail(request, id):
    # //selected room
    room = get_object_or_404(Room, id=id)
    # items in the selected room
    items = room.items.all()
    # show items. we can modify url after discuss
    return render(request, 'room/room_detail.html', {'room': room, 'items': items})