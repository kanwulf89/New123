from rest_framework import serializers
from .models import Cliente2
<<<<<<< HEAD
from .models import OfertaProducto

=======
>>>>>>> 9e4ccb3cd64a0c11aa533cfc17709c09d9667f44


from rest_framework.fields import CurrentUserDefault

class Cliente2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = '__all__'

    


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = '__all__'


       
<<<<<<< HEAD
class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfertaProducto
        fields = '__all__'
=======

>>>>>>> 9e4ccb3cd64a0c11aa533cfc17709c09d9667f44
