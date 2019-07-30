from rest_framework import routers
from .viewsets import ProductoViewSets, ListaProductos2



router = routers.SimpleRouter()
router.register('producto', ProductoViewSets)
router.register('listaproducto',ListaProductos2)


urlpatterns = router.urls