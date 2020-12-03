from django import forms

from .models import Jugador, Equipo, Estadio

class FormCreateJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = [
            "nombre",
            "edad",
            "pisicion",
            "equipo"
        ]

class FormCreateEquipo(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            "nombre",
            "division",
            "estadio",
        ]

class FormCreateEstadio(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = [
            "nombre",
            "capacidad",
            "ciudad",
            "estado",
            "eqlocales"
        ]
