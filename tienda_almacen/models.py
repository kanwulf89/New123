from django.db import models

# Create your models here.


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    cantidad_producto = models.IntegerField()
    precio_unidad = models.DecimalField(null=True, blank=True, default=None, max_digits=19, decimal_places=10)
    descripcion = models.CharField(max_length=200, default="")
    images = models.CharField(max_length=500, default='')
    def __str__(self):
        return self.nombre_producto



class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True, default=None)
    nombre_categoria = models.CharField(max_length=30)

'''

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    p = models.ForeignKey(Producto, on_delete=models.CASCADE, null = True)
    def __str__(self):
        return self.file.name
'''