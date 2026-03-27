"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory.views import item_list, item_detail, item_create, item_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    # Lista de items (y búsqueda)
    path('', item_list, name='item_list'),
    
    # Detalle de item
    path('item/<int:pk>/', item_detail, name='item_detail'),
    
    # Nueva ruta: Añadir item
    path('add/', item_create, name='item_create'),
    
    # Nueva ruta: Eliminar item
    path('delete/<int:pk>/', item_delete, name='item_delete'),

]
