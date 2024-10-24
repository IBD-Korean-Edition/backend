from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from ..Borrow.models import Item
import json

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_item(request, item_name):
    print("Entered")
    try:
        # Delete all items with the given name
        items_deleted, _ = Item.objects.filter(name=item_name).delete()
        print(items_deleted)

        if items_deleted == 0:
            return JsonResponse({'error': 'No items found with the specified name'}, status=404)

        return JsonResponse({'message': f'{items_deleted} item(s) deleted successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
