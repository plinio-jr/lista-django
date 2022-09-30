from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core import views
from core.views import (
    ListaDetail,
    ListaDetailGeneric,
    ListaList,
    ListaViewSet,
    MercadoViewSet,
    ProdutoViewSet,
)
from media.router import router as media_router

router = DefaultRouter()
router.register(r"listas", ListaViewSet)
router.register(r"mercados", MercadoViewSet)
router.register(r"produtos", ProdutoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path('listas/<int:id>', views.Lista),
    path('listas-apiview/', views.ListaList.as_view()),
    path('listas-apiview/<int:id>/', views.ListaDetail.as_view()),
    path('listas-generic/', views.ListasListGeneric.as_view()),
    path('listas-generic/<int:id>/', views.ListaDetailGeneric.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/media/", include(media_router.urls)),
     path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
     path("api/", include(router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)