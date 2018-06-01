from django.urls import path
from .views import *

app_name = 'Productos'
urlpatterns = [
	path('', VisualizarProductos , name='visualizar'),
	path('descripcion/<int:id_producto>', DescripcionProducto , name='descripcion'),
	path('pedido/<int:id_producto>' , RealizarPedido , name='pedido'),
	path('lista_pedidos', VisualizarPedidos , name='pedidos'),
]