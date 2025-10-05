from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Procesador(models.Model):
    diseñador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Ram(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre


class Grafica(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    fecha_salida_mercado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre