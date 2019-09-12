from django.db import models
from tienda_suscripcion.models import Tienda
from tienda_almacen.models import Producto

# Create your models here.


class Pago(models.Model):
    nombre_tarjeta = models.CharField(max_length=20)
    numero_tarjeta = models.CharField(primary_key=True, max_length=40)
    '''Acaba la llave foreanea del cliente'''
  

class Cliente2(models.Model):
    cedula = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=20, default="")
    lastname = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=30, default="")
    phone = models.CharField(max_length=20, default="")
    seller = models.BooleanField(default=False)
    contra = models.CharField(max_length=20,default="")
    

    def __str__(self):
        return self.nombre
   
        



   

class Pedido(models.Model):
    numero_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente2, blank=True, on_delete=models.CASCADE)
    
''' clases Oferta y Compra nuevos, que describen? existe una relacion articulo,tienda(vendedor) oferta'''
''' Esta relacion me permite que para cada oferta en la tienda se tenga una clase compra que se asigna a oferta'''
'''Esta compra la realiza un CLiente y a su vez la clase compra gerenra una factura y un envio'''



class Factura(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    date = models.DateField()
    precioTotal = models.BigIntegerField()
    nombre_cliente = models.CharField(max_length=20)
    comprax = models.CharField(max_length=20, default="")


class Envio(models.Model):
    id_envio = models.IntegerField(primary_key=True)
    dir_destino = models.CharField(max_length=30)
    precio_envio = models.IntegerField()
    date = models.DateField()
    hora = models.DateTimeField()
    factura = models.ForeignKey(Factura, blank=True, on_delete=models.CASCADE)



        
'''MODELADO DE PRUEBA '''
'''
class ClienteOferta(models.Model):
    tienday = models.ForeignKey(Cliente2, blank=True, on_delete=models.CASCADE)
    productoy = models.ForeignKey(Producto, blank=True, on_delete=models.CASCADE)
    ofertx = models.AutoField(primary_key=True, default=False)
'''

class Compra(models.Model):
    numero_compra = models.CharField(max_length=30)
    oferta = models.CharField(max_length = 30)




   

class Oferta(models.Model):
    booleano = models.BooleanField(default=False)
    ofertaz = models.CharField(max_length=20)



class PseudoJoin(models.Model):
    vendedor = models.ForeignKey(Cliente2, on_delete=models.CASCADE)
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE, null = True)
    pedidos = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)
