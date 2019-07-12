from django.db import models

from tienda_suscripcion.models import Tienda
from tienda_almacen.models import Producto

# Create your models here.


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=30)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)

class Pedido(models.Model):
    numero_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, blank=True, on_delete=models.CASCADE)

class Factura(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    date = models.DateField()
    precioTotal = models.BigIntegerField()
    nombre_cliente = models.CharField(max_length=20)
    pedido = models.ForeignKey(Pedido, blank=True, on_delete=models.CASCADE, default=0)


class Envio(models.Model):
    id_envio = models.IntegerField(primary_key=True)
    dir_destino = models.CharField(max_length=30)
    precio_envio = models.IntegerField()
    date = models.DateField()
    hora = models.DateTimeField()
    factura = models.ForeignKey(Factura, blank=True, on_delete=models.CASCADE)

class Venta(models.Model):
    tienday = models.ForeignKey(Tienda, blank=True, on_delete=models.CASCADE)
    productoy = models.ForeignKey(Producto, blank=True, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, blank=True, on_delete=models.CASCADE, default=0)




