from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Item

def item_list(request):
    """
    Lista todos los ítems o filtra por búsqueda si se recibe el parámetro 'q'.
    """
    query = request.GET.get('q', '') 
    if query:
        # Filtramos por nombre, marca o descripción sin distinguir mayúsculas
        items = Item.objects.filter(
            Q(name__icontains=query) | 
            Q(brand__icontains=query) | 
            Q(description__icontains=query)
        )
    else:
        items = Item.objects.all()
    
    return render(request, 'inventory/item_list.html', {
        'items': items, 
        'query': query
    })

def item_detail(request, pk):
    """
    Muestra los detalles de un ítem específico.
    """
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'inventory/item_detail.html', {'item': item})

def item_create(request):
    """
    Maneja la creación de nuevos ítems desde el formulario.
    """
    if request.method == 'POST':
        Item.objects.create(
            name=request.POST.get('name'),
            brand=request.POST.get('brand'),
            description=request.POST.get('description'),
        )
        return redirect('item_list')
    return render(request, 'inventory/item_form.html')

def item_delete(request, pk):
    """
    Elimina un ítem y redirige a la lista principal.
    """
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
    return redirect('item_list')