from django.contrib import admin

# Register your models here.
from .models import Jugador, Equipo, Estadio

admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Estadio)
