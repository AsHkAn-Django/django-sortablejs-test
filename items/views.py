from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Item


def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})


@csrf_exempt  # We'll handle CSRF more securely later
def reorder_items(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            order = data.get('order', [])

            for index, item_id in enumerate(order):
                item = Item.objects.get(id=item_id)
                item.order = index
                item.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)