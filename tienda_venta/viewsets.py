from rest_framework import viewsets
<<<<<<< HEAD
from .serializer import Cliente2Serializer, LoginSerializer, OfertaSerializer
=======
from .serializer import Cliente2Serializer, LoginSerializer
>>>>>>> 9e4ccb3cd64a0c11aa533cfc17709c09d9667f44
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente2

<<<<<<< HEAD
from .models import OfertaProducto
=======
from .models import Oferta
>>>>>>> 9e4ccb3cd64a0c11aa533cfc17709c09d9667f44



class ClienteViewSets(viewsets.ModelViewSet):
    queryset = Cliente2.objects.all()
    serializer_class = Cliente2Serializer

class ClienteLogin(viewsets.ModelViewSet):
    
    queryset = Cliente2.objects.all()
    serializer_class = LoginSerializer


<<<<<<< HEAD
class OfertaViewSets(viewsets.ModelViewSet):
    queryset = OfertaProducto.objects.all()
    serializer_class = OfertaSerializer

=======


>>>>>>> 9e4ccb3cd64a0c11aa533cfc17709c09d9667f44

