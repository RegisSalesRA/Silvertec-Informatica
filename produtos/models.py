from django.db import models
from acessorios.models import Cores, Coolers


# Create your models here.

class Processador(models.Model):
    INTEL = 'INTEL'
    AMD = 'AMD'
    INTEL_AMD = 'INTEL E AMD'

    marcas_opcoes = [
        (INTEL, 'INTEL'),
        (AMD, 'AMD'),
        (INTEL_AMD, 'INTEL E AMD')
    ]

    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, choices=marcas_opcoes)
    descricao = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = "Processadores"

    def __str__(self):
        return self.descricao


class PlacaMae(models.Model):
    INTEL = 'INTEL'
    AMD = 'AMD'
    INTEL_AMD = 'INTEL E AMD'

    marcas_opcoes = [
        (INTEL, 'INTEL'),
        (AMD, 'AMD'),
        (INTEL_AMD, 'INTEL E AMD')
    ]

    memoria_opcoes = [
        (8,8),
        (16,16),
        (32,32),
        (64,64),
    ]

    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=100, choices=marcas_opcoes)
    slots = models.IntegerField(default=0)
    memoria_suportada = models.PositiveIntegerField(choices=memoria_opcoes)
    video_integrado = models.BooleanField(default=False)
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Placa Mãe'
        verbose_name_plural = "Placas Mãe"

    def __str__(self):
        return self.descricao


class MemoriaRam(models.Model):
    memoria_opcoes = [
        (8,8),
        (16,16),
        (32,32),
        (64,64),
    ]
    
    nome = models.CharField(max_length=150)
    memoria = models.PositiveIntegerField(choices=memoria_opcoes)
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Memoria'
        verbose_name_plural = "Memorias"

    def __str__(self):
        return self.descricao


class PlacaDeVideo(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Placa de video'
        verbose_name_plural = "Placas de video"

    def __str__(self):
        return self.descricao