from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Jugador, Equipo, Estadio
from .forms import FormCreateJugador, FormCreateEquipo, FormCreateEstadio
# Create your views here.

class Index(generic.TemplateView):
    template_name = "NFLP/index.html"

#---------------------------------------------------------------------->

class ListJugador(generic.ListView):
    template_name = "NFLP/listjugador.html"
    queryset = Jugador.objects.all().order_by('id')


class DetailJugador(generic.DetailView):
    template_name = "NFLP/detailjugador.html"
    model = Jugador


class UpdateJugador(generic.UpdateView):
    template_name = "NFLP/updatejugador.html"
    model = Jugador
    form_class = FormCreateJugador
    success_url = reverse_lazy("NFLP:listjugadores")

#--------------------------------------------------------------------------->

class ListEquipo(generic.ListView):
    template_name = "NFLP/listequipo.html"
    queryset = Equipo.objects.all().order_by('id')


class DetailEquipo(generic.DetailView):
    template_name = "NFLP/detailequipo.html"
    model = Equipo


class UpdateEquipo(generic.UpdateView):
    template_name = "NFLP/updateequipo.html"
    model = Equipo
    form_class = FormCreateEquipo
    success_url = reverse_lazy("NFLP:listequipo")

#--------------------------------------------------------------------------->

class ListEstadio(generic.ListView):
    template_name = "NFLP/listestadio.html"
    queryset = Estadio.objects.all().order_by('id')


class DetailEstadio(generic.DetailView):
    template_name = "NFLP/detailestadio.html"
    model = Estadio


class UpdateEstadio(generic.UpdateView):
    template_name = "NFLP/updateestadio.html"
    model = Estadio
    form_class = FormCreateEstadio
    success_url = reverse_lazy("NFLP:listestadio")

#--------------------------------------------------------------------------->
