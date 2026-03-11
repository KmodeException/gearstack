from django.contrib import admin
from .models import Item, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'purchase_date']
    list_filter = ['category', 'brand']
    search_fields = ['name', 'serial_number']
