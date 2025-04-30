from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_protect  

from .models import Item


def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})


@csrf_protect
def reorder_items(request):
    """
    Accepts a JSON POST request with a list of item IDs in new order.
    Updates each item's 'order' field to reflect the new order.
    """
    try:
        # Parse JSON request body into Python dictionary
        data = json.loads(request.body)

        # Extract the 'order' list from the data
        order = data.get('order', [])

        # Update each item in the database
        for index, item_id in enumerate(order):
            item = Item.objects.get(id=item_id)
            item.order = index
            item.save()

        # Respond with success
        return JsonResponse({'status': 'success'})
    except Exception as e:
        # If something goes wrong, respond with an error
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)