from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, CuentaViewSet, MovimientoViewSet, RegisterView 
from django.urls import path

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'cuentas', CuentaViewSet)
router.register(r'movimientos', MovimientoViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('register/', RegisterView.as_view(), name='register'),
]