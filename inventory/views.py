from django.shortcuts import render
from .models import Item
from django.shortcuts import render, get_object_or_404

def item_list(request):
    items = Item.objects.all()
    return render(request, 'inventory/item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'inventory/item_detail.html', {'item': item})