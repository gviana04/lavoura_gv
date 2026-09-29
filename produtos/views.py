from rest_framework import viewsets
from .models import Fazenda, Lavoura
from .serializers import FazendaSerializer, LavouraSerializer
class FazendaViewSet(viewsets.ModelViewSet):
    queryset = Fazenda.objects.all()
    serializer_class = FazendaSerializer
class LavouraViewSet(viewsets.ModelViewSet):
    queryset = Lavoura.objects.all()
    serializer_class = LavouraSerializer