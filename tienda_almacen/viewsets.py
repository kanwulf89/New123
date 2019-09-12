from rest_framework import viewsets
from .models import Producto, File
from .serializer import ProductoSerializer, FileSerializer, GuardaProducto, EditaCantidad
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from .serializer import CategoriaSerializer
from .models import Categoria




class ProductoViewSets(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    '''
    INventarse un trigger aca para llenar la tupla idproducto con la idauto de django
    queryset2 = Producto.objects.filter(id_producto=5)
    queryset2.delete()'''
   
    serializer_class = ProductoSerializer


class ListaProductos2(viewsets.ModelViewSet):
    queryset = Producto.objects.all()[4:]
    serializer_class = ProductoSerializer


class FileGuarda(viewsets.ModelViewSet):
    queryset = File.objects.all()
   
    serializer_class = FileSerializer
    
class EditacantidaP(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = EditaCantidad

class CategoriaViewSets(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()   
    serializer_class = CategoriaSerializer
   


class GuardaProductos(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    
    serializer_class = GuardaProducto
