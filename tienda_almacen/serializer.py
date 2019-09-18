from rest_framework import serializers
from .models import Producto, File, Categoria




class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'id_categoria', 'nombre_categoria')

'''Guarda producto solo '''


class GuardaProducto(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = ('url','id_producto','nombre_producto','cantidad_producto','precio_unidad','descripcion','categoria_id')


class EditaCantidad(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['cantidad_producto']


class FileSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = File
        fields = ('id','url','file','p')

class ProductoSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)
    categoria_id = CategoriaSerializer()
    class Meta:
        model = Producto
        fields = ('url','id_producto','nombre_producto','cantidad_producto','precio_unidad','descripcion','categoria_id','files')
        def create(self, validated_data):
            files_data = validated_data.pop('files')
            productos = Producto.objects.create(**validated_data)
            for file_data in files_data:
                File.objects.create(Producto2=productos, **file_data)
            return productos

