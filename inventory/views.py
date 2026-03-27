from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Item


def item_list(request):
    items = Item.objects.all()
    return render(request, 'inventory/item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'inventory/item_detail.html', {'item': item})

def item_create(request):
    if request.method == 'POST':
        Item.objects.create(
            name=request.POST.get('name'),
            brand=request.POST.get('brand'),
            description=request.POST.get('description'),
        )
        return redirect('item_list')
    return render(request, 'inventory/item_form.html')

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'inventory/item_list.html', {'item': item})

def item_list(request):
    # Capturamos lo que el usuario escribe en el input name="q"
    query = request.GET.get('q', '') 
    
    if query:
        # Filtramos por nombre, marca o descripción (icontains no distingue mayúsculas)
        items = Item.objects.filter(
            Q(name__icontains=query) | 
            Q(brand__icontains=query) | 
            Q(description__icontains=query)
        )
    else:
        # Si no hay búsqueda, mostramos todo como hasta ahora
        items = Item.objects.all()
    
    return render(request, 'inventory/item_list.html', {
        'items': items, 
        'query': query  # Enviamos la query de vuelta para que no se borre del input
    })
