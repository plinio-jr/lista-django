from django.db import models

from media.models import Image

from .produto import Produto


class Lista(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="+")
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.nome} ({self.descricao})"

        