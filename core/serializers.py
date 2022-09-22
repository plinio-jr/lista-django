from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from core.models import Lista, Mercado, Produto

class ListaSerializer(ModelSerializer):
    class Meta:
        model = Lista
        fields = "__all__"

class MercadoSerializer(ModelSerializer):
    class Meta:
        model = Mercado
        fields = "__all__"

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"