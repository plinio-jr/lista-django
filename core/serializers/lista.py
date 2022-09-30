from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Lista
from media.models import Image
from media.serializers import ImageSerializer

from .lista import Lista


class ListaSerializer(ModelSerializer):
    class Meta:
        model = Lista
        fields = "__all__"
        capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class ListaDetailSerializer(ModelSerializer):
         capa = ImageSerializer(required=False)