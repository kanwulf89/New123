from rest_framework import routers
from .viewsets import ClienteViewSets
from .viewsets import ClienteLogin
<<<<<<< HEAD
from .viewsets import OfertaViewSets
=======
>>>>>>> 9e4ccb3cd64a0c11aa533cfc17709c09d9667f44


router = routers.SimpleRouter()
router.register('clientes', ClienteViewSets)
router.register('busca', ClienteLogin)
<<<<<<< HEAD
router.register('Oferta',OfertaViewSets)
=======
>>>>>>> 9e4ccb3cd64a0c11aa533cfc17709c09d9667f44





urlpatterns = router.urls

'''
urlpatterns= [
    url(r'^tienda_venta/$',views.Login)
]'''


