from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from .models import Producto , Pedido

def VisualizarProductos(request):
    template = get_template('productos_app/visualizar_productos.html')
    ctx = {}

    if request.method == 'GET':
         productos = Producto.objects.all()
         ctx = {
             'productos': productos,
         }

    return HttpResponse(template.render(ctx,request))

def DescripcionProducto(request, id_producto):
    template = get_template('productos_app/descripcion.html')
    ctx = {}

    if request.method == 'GET':
        producto = Producto.objects.get(id = id_producto)
        ctx = {
            'producto': producto,
        }
    return HttpResponse(template.render(ctx,request))

def RealizarPedido(request, id_producto):
    template = get_template('productos_app/pedido.html')
    producto = Producto.objects.get(id = id_producto)
    flag_done = False
    ctx = {
        'producto': producto,
    }

    if request.method == 'POST':
        flag_done = True
        id_producto = request.POST.get('id_producto')
        producto = Producto.objects.get(id=id_producto)
        cantidad = request.POST.get('cantidad')
        tipo = request.POST.get('tipo')
        observaciones = request.POST.get('observaciones')
        nombre = request.POST.get('nombre_cliente')
        pedido = Pedido(producto_id=id_producto,nombre_cliente=nombre, cantidad=cantidad , tipo=tipo, observacion=observaciones, precio=(int(producto.precio) * int(cantidad)))
        pedido.save()
        ctx = {
        'flag': flag_done,
        }

    return HttpResponse(template.render(ctx,request))

def VisualizarPedidos(request):
    template = get_template('productos_app/pedidos.html')
    pedidos = Pedido.objects.all()
    ctx = {
        'pedidos': pedidos,
    }
    return HttpResponse(template.render(ctx,request))

def Index(request):
    template = get_template('productos_app/index.html')
    ctx = {}
    return HttpResponse(template.render(ctx,request))