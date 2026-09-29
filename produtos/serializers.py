from rest_framework import serializers
from .models import Fazenda, Lavoura

class LavouraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lavoura
        fields = '__all__'
class FazendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fazenda
        fields = '__all__'