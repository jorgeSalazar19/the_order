from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from .models import Producto , Pedido , Restaurante

def VisualizarProductos(request, id_resturante):
    template = get_template('productos_app/visualizar_productos.html')
    restaurante = Restaurante.objects.get(id=id_resturante)
    ctx = {}

    if request.method == 'GET':
         productos = restaurante.productos.all()
         ctx = {
             'productos': productos,
             'restaurante': restaurante
         }

    return HttpResponse(template.render(ctx,request))

def DescripcionProducto(request,id_resturante ,id_producto):
    template = get_template('productos_app/descripcion.html')
    restaurante = Restaurante.objects.get(id=id_resturante)
    ctx = {}

    if request.method == 'GET':
        producto = Producto.objects.get(id = id_producto)
        ctx = {
            'producto': producto,
            'restaurante': restaurante
        }
    return HttpResponse(template.render(ctx,request))

def RealizarPedido(request, id_resturante, id_producto):
    template = get_template('productos_app/pedido.html')
    producto = Producto.objects.get(id = id_producto)
    restaurante = Restaurante.objects.get(id=id_resturante)
    flag_done = False
    ctx = {
        'producto': producto,
        'restaurante': restaurante

    }

    if request.method == 'POST':
        flag_done = True
        id_producto = request.POST.get('id_producto')
        producto = Producto.objects.get(id=id_producto)
        cantidad = request.POST.get('cantidad')
        tipo = request.POST.get('tipo')
        observaciones = request.POST.get('observaciones')
        nombre = request.POST.get('nombre_cliente')
        pedido = Pedido(producto_id=id_producto,nombre_cliente=nombre, cantidad=cantidad , tipo=tipo, observacion=observaciones, precio=(int(producto.precio) * int(cantidad)) , estado_pedido='En espera')
        pedido.save()
        ctx = {
            'flag': flag_done,
            'restaurante': restaurante
        }

    return HttpResponse(template.render(ctx,request))

def VisualizarPedidos(request, id_resturante):
    template = get_template('productos_app/pedidos.html')
    restaurante = Restaurante.objects.get(id=id_resturante)
    pedidos = Pedido.objects.all()
    ctx = {
        'pedidos': pedidos,
        'restaurante':restaurante
    }
    return HttpResponse(template.render(ctx,request))

def Index(request):
    template = get_template('productos_app/index.html')
    restaurante = Restaurante.objects.get(id=1)
    ctx = {
        'restaurante': restaurante
    }
    return HttpResponse(template.render(ctx,request))