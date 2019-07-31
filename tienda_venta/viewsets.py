from rest_framework import viewsets
from .serializer import Cliente2Serializer, LoginSerializer
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente2

from .models import Oferta



class ClienteViewSets(viewsets.ModelViewSet):
    queryset = Cliente2.objects.all()
    serializer_class = Cliente2Serializer

class ClienteLogin(viewsets.ModelViewSet):
    
    queryset = Cliente2.objects.all()
    serializer_class = LoginSerializer





