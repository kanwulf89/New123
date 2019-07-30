from rest_framework import routers
from .viewsets import ClienteViewSets
from .viewsets import ClienteLogin
from .viewsets import OfertaViewsets
from .viewsets import Oferta1Viewsets

router = routers.SimpleRouter()
router.register('clientes', ClienteViewSets)
router.register('busca', ClienteLogin)
router.register('Oferta', OfertaViewsets)
router.register('Oferta1', Oferta1Viewsets)




urlpatterns = router.urls

'''
urlpatterns= [
    url(r'^tienda_venta/$',views.Login)
]'''


