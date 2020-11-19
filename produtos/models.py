from django.db import models
from informacoes.models import Marcas, Tamanhos
from acessorios.models import Cores
from django.db.models.deletion import CASCADE
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager


# Create your models here.

class Processador(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = "Processadores"

    def __str__(self):
        return f'{self.nome} {self.marca}'


class PlacaMae(models.Model):
    memoria_suportada = [
        ('opcao1', 'Até 16 GB'),
        ('opcao2', 'Até 64 GB'),
    ]

    slots = [
        ('2', '2'),
        ('4', '4'),
    ]

    nome = models.CharField(max_length=150)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    slots = models.CharField(choices=slots, max_length=20)
    memoriaSuportada = models.CharField(choices=memoria_suportada, max_length=100)
    videoIntegrado = models.BooleanField(default=False)
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Placa Mãe'
        verbose_name_plural = "Placas Mãe"

    def __str__(self):
        return f'{self.nome} {self.marca} {self.slots} {self.memoriaSuportada} {self.videoIntegrado}'


class MemoriaRam(models.Model):
    nome = models.CharField(max_length=150)
    tamanho = models.ForeignKey(Tamanhos, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Memoria'
        verbose_name_plural = "Memorias"

    def __str__(self):
        return f'{self.nome} {self.tamanho}'


class PlacaDeVideo(models.Model):
    nome = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Placa de video'
        verbose_name_plural = "Placas de video"

    def __str__(self):
        return self.nome
