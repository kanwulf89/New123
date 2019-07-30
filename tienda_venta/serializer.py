from rest_framework import serializers
from .models import Cliente2
from .models import ClienteOferta
from .models import Oferta
from rest_framework.fields import CurrentUserDefault

class Cliente2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = '__all__'

    


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = '__all__'


       
class OfertaViewsets(serializers.ModelSerializer):
    class Meta:
        model = ClienteOferta
        fields = '__all__'

class Oferta1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'