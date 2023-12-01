from django.db import models
from django.contrib.auth.models import AbstractUser

class Gerente(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.BigIntegerField()
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=30)
    rua = models.CharField(max_length=140)
    nm_casa = models.IntegerField()

    class Meta:
        verbose_name_plural = "Gerentes"
        ordering = ('nome',)


    def __str__(self) -> str:
        return self.nome


class Garçom(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.BigIntegerField()
    telefone = models.CharField(max_length=11)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=30)
    rua = models.CharField(max_length=140)
    nm_casa = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Garçons"
        ordering = ('nome',)


    def __str__(self) -> str:
        return self.nome