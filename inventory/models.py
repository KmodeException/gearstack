from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de Categoría")
    description = models.TextField(blank=True, verbose_name="Descripción")

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del Ítem")
    # Agregamos null=True y blank=True para que el MVP no rompa si no eliges categoría aún
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoría")
    brand = models.CharField(max_length=100, blank=True, verbose_name="Marca")
    serial_number = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="Número de Serie")
    purchase_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Adquisición")
    # Cambiamos notes por description o viceversa para que coincida con la vista
    description = models.TextField(blank=True, verbose_name="Descripción / Notas") 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.brand if self.brand else 'Sin marca'})"