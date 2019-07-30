from rest_framework import viewsets
from .serializer import Cliente2Serializer, LoginSerializer, OfertaViewsets, Oferta1Serializer
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente2
from .models import ClienteOferta
from .models import Oferta



class ClienteViewSets(viewsets.ModelViewSet):
    queryset = Cliente2.objects.all()
    serializer_class = Cliente2Serializer

class ClienteLogin(viewsets.ModelViewSet):
    
    queryset = Cliente2.objects.all()
    serializer_class = LoginSerializer


class OfertaViewsets(viewsets.ModelViewSet):
    queryset = ClienteOferta.objects.all()
    serializer_class = OfertaViewsets

class Oferta1Viewsets(viewsets.ModelViewSet):
     queryset = Oferta.objects.all()
     serializer_class = Oferta1Serializer  

