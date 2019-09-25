from rest_framework import serializers
from django.db import models
from .models import Cliente2
from .models import PseudoJoin, Pedido, Join2, Factura2
from tienda_almacen.models import Producto 
from tienda_almacen.serializer import ProductoSerializer, FileSerializer


from rest_framework.fields import CurrentUserDefault



class Cliente2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = ('url','cedula','nombre','url','lastname','email','phone','seller','contra')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = ('cedula','nombre','lastname','email','phone')

   


class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PseudoJoin
        fields = '__all__'

'''guarda en la tabla vendedor-producto-pedido-factura'''
class OfertaSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Join2
        fields = '__all__'

class JoinFalso(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PseudoJoin
        fields = ('id','url','vendedor','productos','pedidos')

'''Guarda el pedido'''
class PedidoSerializerGuarda(serializers.ModelSerializer):
    
    class Meta:
        model = Pedido
        fields = ('numero_pedido','cliente')


'''vistas de pedido'''
class PedidoSerializer(serializers.ModelSerializer):
    cliente = LoginSerializer()
    class Meta:
        model = Pedido
        fields = ('numero_pedido','cliente')

'''Crea la tabla Oferta o carrito de compras'''
class JoinFalso2(serializers.ModelSerializer):
    vendedor = LoginSerializer()
    productos = ProductoSerializer()
   

    class Meta:
        model = PseudoJoin
        fields = ('id','url','vendedor','productos')


'''llenar factura normal '''
class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura2
        fields = ('numero_factura','saldoTotal','created_at')


'''Crea la tabla para compras y facturas'''

'''Existe una redundancia de datos ya que pasar en el serializer a facturax = su realizer es redundate'''
'''Por que? porque dentro del modelo factura en el atributo factura con el related_name ya estoy apuntando que todo'''
'''el modelo de la tabla join2 que contiene id vendedor, idproductos, idpedido, y es una subclase de factura'''
''' es decir todos los datos del vendedor que vende x productos bajo x pedido va a estar almacenado o anidado '''
'''sobre una unica factura'''


class JoinFalso3(serializers.ModelSerializer):
    vendedor1 = LoginSerializer()
    producto1 = ProductoSerializer()
    pedido1 =   PedidoSerializer()
    facturax = FacturaSerializer()

    class Meta:
        model = Join2
        fields = ('id','vendedor1','producto1','pedido1','facturax')


class FacturaFull(serializers.ModelSerializer):
    join2 = JoinFalso3(many=True)

    class Meta:
        model = Factura2
        fields = ('numero_factura','saldoTotal','created_at','join2')
        def create(self, validated_data):
            files_data = validated_data.pop('join2')
            facturas = Factura2.objects.create(**validated_data)
            for file_data in files_data:
                JoinFalso3.objects.create(facturasx=facturas, **file_data)
            return facturas




