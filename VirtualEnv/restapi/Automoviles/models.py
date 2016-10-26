from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=30)
    creador = models.CharField(max_length=20)


class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete = models.CASCADE)
    color = models.CharField(max_length = 15)
    modelo = models.IntegerField()
    tipo = models.CharField(max_length = 10)
