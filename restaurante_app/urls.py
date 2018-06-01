from django.urls import path
from .views import *

app_name = 'Restaurante'
urlpatterns = [
	path('<int:id_resturante>', VisualizarProductos , name='visualizar'),
	path('descripcion/<int:id_resturante>/<int:id_producto>', DescripcionProducto , name='descripcion'),
	path('pedido/<int:id_resturante>/<int:id_producto>' , RealizarPedido , name='pedido'),
	path('lista_pedidos/<int:id_resturante>', VisualizarPedidos , name='pedidos'),
]