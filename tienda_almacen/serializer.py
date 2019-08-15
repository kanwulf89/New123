from rest_framework import serializers
from .models import Producto

'''Serializer para guardar'''

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url','id_producto','nombre_producto','cantidad_producto','precio_unidad','descripcion','images')

'''

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('id','url','file','p')'''