from rest_framework import viewsets
from .models import Producto
from .serializer import ProductoSerializer

class ProductoViewSets(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    
    '''queryset2 = Producto.objects.filter(id_producto=5)
    queryset2.delete()'''
    serializer_class = ProductoSerializer


class ListaProductos2(viewsets.ModelViewSet):
    queryset = Producto.objects.all()[4:]
    serializer_class = ProductoSerializer

  