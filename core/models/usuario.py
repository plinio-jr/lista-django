from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    nome = models.CharField(max_length=50, blank=True)
    sobrenome = models.CharField(max_length=100, blank=True)
    email = models.DateField(max_length=200)