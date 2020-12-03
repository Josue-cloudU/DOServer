from django.db import models
from django.db.models import Model
# Create your models here.

class Jugador(models.Model):
    nombre = models.CharField(max_length=64)
    edad = models.IntegerField()
    pisicion = models.CharField(max_length=20)
    equipo = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Jugadores"

    def __str__(self):
        return self.nombre


class Equipo(models.Model):
    nombre = models.CharField(max_length=64)
    division = models.CharField(max_length=40)
    estadio = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre


class Estadio(models.Model):
    nombre = models.CharField(max_length=64)
    capacidad = models.IntegerField()
    ciudad = models.CharField(max_length=64)
    estado = models.CharField(max_length=64)
    eqlocales = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
