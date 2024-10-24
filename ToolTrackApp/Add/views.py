from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
import json
from ToolTrackApp.Borrow.models import Item
from ToolTrackApp.Room.models import Room

@csrf_exempt 
@require_http_methods(["POST"])
def add_item(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        room_id = data.get('roomId')
        amount = data.get('amount')

        print(room_id)
        if not name:
            return JsonResponse({'message': 'Name is required'}, status=400)
        if not room_id:
            return JsonResponse({'message': 'Room ID is required'}, status=400)

        # Get the room object
        room = get_object_or_404(Room, number=room_id)

        # Create the item
        for i in range (0,amount):
            item = Item.objects.create(name=name)

        # Associate the item with the room
        room.items.add(item)
        room.save()

        return JsonResponse({'message': 'Item added successfully'}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)
