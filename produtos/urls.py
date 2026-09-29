from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FazendaViewSet, LavouraViewSet

router = DefaultRouter()
router.register(r'fazendas', FazendaViewSet)
router.register(r'lavouras', LavouraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]