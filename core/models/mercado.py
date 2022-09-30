from django.db import models


class Mercado(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    avaliacao = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.nome
