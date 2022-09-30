from django.db import models

from .mercado import Mercado


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50, blank= True, null=True)
    quantidade = models.IntegerField(null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    mercado = models.ForeignKey(
        Mercado, on_delete=models.PROTECT, related_name="produtos"
    )

    def __str__(self):
        return self.nome