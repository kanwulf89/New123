from rest_framework import routers
from .viewsets import ClienteViewSets
from .viewsets import ClienteLogin
from .viewsets import viewjoin
from .viewsets import OfertaViewSets
from .viewsets import VistaPrueba,VistaPrueba2,PruebaProducto
from .models import Cliente2
from .serializer import LoginSerializer
from tienda_almacen.models import Producto 
from tienda_almacen.serializer import ProductoSerializer, FileSerializer

router = routers.SimpleRouter()
router.register('clientes', ClienteViewSets)
router.register('busca', ClienteLogin, base_name=Cliente2)

router.register('Oferta',OfertaViewSets)
'''Join entre vendedor producto y foto de producto'''
router.register('test',viewjoin)
router.register('test1',VistaPrueba)
router.register('test2',VistaPrueba2, base_name=Producto)
'''prueba'''
router.register('test10',PruebaProducto)





urlpatterns = router.urls

'''
urlpatterns= [
    url(r'^tienda_venta/$',views.Login)
]'''


