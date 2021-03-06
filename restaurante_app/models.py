from django.db import models

class Producto(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=200)
	imagen=models.ImageField(upload_to="productos", null=True, blank=True, default=None)
	precio=models.BigIntegerField(default=0)

	def __str__(self):
		return "Producto: " + self.nombre

class Pedido(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	nombre_cliente = models.CharField(max_length=50, default=None)
	cantidad = models.IntegerField(default=0)
	observacion = models.CharField(max_length=200)
	tipo = models.CharField(max_length=50)
	precio = models.BigIntegerField(default=0)
	estado_pedido = models.CharField(max_length=50, default=None)

	def __str__(self):
		return "Pedido: " + self.nombre_cliente

class Restaurante(models.Model):
	productos = models.ManyToManyField(Producto)
	nombre = models.CharField(max_length=50)
	logo = models.ImageField(upload_to="logos", null=True, blank=True, default=None)

	def __str__(self):
		return "Restaurante: " + self.nombre
