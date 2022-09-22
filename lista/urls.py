from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core.views import ListaViewSet
from core.views import MercadoViewSet
from core.views import ProdutoViewSet

router = DefaultRouter()
router.register(r"listas", ListaViewSet)
router.register(r"mercados", MercadoViewSet)
router.register(r"produtos", ProdutoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
