from rest_framework import routers
from .viewsets import ProductoViewSets, ListaProductos2, FileGuarda, GuardaProductos,EditacantidaP
from .viewsets import CategoriaViewSets



router = routers.SimpleRouter()
router.register('listaproducto',ListaProductos2)
router.register('producto', ProductoViewSets)
router.register('guardafoto', FileGuarda)
router.register('gp',GuardaProductos)
router.register('categoria', CategoriaViewSets)
router.register('edicanti',EditacantidaP)


urlpatterns = router.urls