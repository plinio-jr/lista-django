from rest_framework.serializers import ModelSerializer

from core.models import Mercado

from .mercado import Mercado


class MercadoSerializer(ModelSerializer):
    class Meta:
        model = Mercado
        fields = "__all__"
