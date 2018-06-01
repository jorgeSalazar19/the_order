from django.contrib import admin
from .models import Producto, Pedido , Restaurante

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','precio']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['producto','tipo']

@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
	list_display = ['nombre']


