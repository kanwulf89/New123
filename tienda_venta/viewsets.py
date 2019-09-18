from rest_framework import viewsets
from .serializer import Cliente2Serializer, LoginSerializer,OfertaSerializer2,PedidoSerializerGuarda, FacturaSerializer,JoinFalso3,OfertaSerializer, JoinFalso, JoinFalso2, PedidoSerializer
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente2,PseudoJoin, Pedido, Join2, Factura2
from tienda_almacen.models import Producto 
from tienda_almacen.serializer import ProductoSerializer, FileSerializer
from .models import Oferta
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response




class ClienteViewSets(viewsets.ModelViewSet):

    
    queryset = Cliente2.objects.all()
  
    serializer_class = Cliente2Serializer

class ClienteLogin(viewsets.ModelViewSet):
    queryset = Cliente2.objects.all()
    serializer_class = LoginSerializer
    
'''Guarda datos en la tabla de la relacion ternaria vendedor,productos,pedido'''
class Compra(viewsets.ModelViewSet):
    queryset = Join2.objects.all()
    serializer_class = OfertaSerializer2
   

    
'''prueba'''

class PruebaProducto(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class OfertaViewSets(viewsets.ModelViewSet):
    queryset = PseudoJoin.objects.all()
    serializer_class = OfertaSerializer


'''Join entre Modelo cliente oferta y Productos'''
class viewjoin(viewsets.ModelViewSet):

    queryset = PseudoJoin.objects.all()
    serializer_class = JoinFalso

class VistaPrueba(viewsets.ModelViewSet):
    queryset = PseudoJoin.objects.all()[:4]
    serializer_class = JoinFalso2

class VistaPrueba2(viewsets.ModelViewSet):
    queryset = PseudoJoin.objects.all()
    serializer_class = JoinFalso2


class PedidoVista(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoGuarda(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    
    serializer_class = PedidoSerializerGuarda
    

class VistaPrueba3(viewsets.ModelViewSet):
    queryset = Join2.objects.all()
    serializer_class = JoinFalso3
'''
class ListaFacturas(viewsets.ModelViewSet):
    queryset = Factura2.objects.all()
    
    serializer_class = FacturaFull'''

class GuardaFactura(viewsets.ModelViewSet):
    queryset = Factura2.objects.all()
   
    serializer_class = FacturaSerializer

''' queryset.delete()'''