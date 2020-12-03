from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import generic
from django.urls import reverse_lazy

from .serializers import UserListSerializer, SavingListSerializer, SavingSerializer, UserSerializer

from .forms import FormSaving, FormUser
import requests

from savings.models import Cundina
from .models import User
# Create your views here.

class Index(generic.TemplateView):
    template_name = "savings/indexs.html"
#-----------------------------------------------------------------------------------------------------------

def list_Users(request):
    url = "http://localhost:8000/list_users/"
    response = requests.get(url)
    obj = response.json()
    context = {
        "objs":obj
    }
    return render(request, "savings/list_users.html", context)

class ListUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

def list_Saving(request):
    url = "http://localhost:8000/list_saving/"
    response = requests.get(url)
    obj = response.json()
    context = {
        "objs":obj
    }
    return render(request, "savings/list_saving.html", context)

class ListSaving(generics.ListCreateAPIView):
    queryset = Cundina.objects.all()
    serializer_class = SavingListSerializer

def createCundina(request):
    form = FormSaving(request.POST)
    if request.method=='POST':
        form = FormSaving(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            user_update = form.cleaned_data['user_update']
            status = form.cleaned_data['status']
            descripcion = form.cleaned_data['descripcion']
            cantahorro = form.cleaned_data['cantahorro']
            nparticipantes = form.cleaned_data['nparticipantes']
            url = "http://localhost:8000/saving_create/"
            payload = {
                "user": user_id,
                "user_update": user_update,
                "status": status,
                "descripcion": descripcion,
                "cantahorro": cantahorro,
                "nparticipantes": nparticipantes

            }
            response = requests.post(url, data=payload)
            return redirect('savings:saving_list')
            #print("User: {0}".format(user_id))
    form = FormSaving()
    context = {
        "form": form
    }

    return render(request, "savings/new_cundina.html", context)

class SavingCreate(generics.CreateAPIView):
    serializer_class = SavingSerializer

def createUser(request):
    form = FormUser(request.POST)
    if request.method=='POST':
        form = FormUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            url = "http://localhost:8000/user_create/"
            payload = {
                "username": username,
                "email": email,
                "password": password,
            }
            response = requests.post(url, data=payload)
            return redirect('gallery:index')
            #print("User: {0}".format(user_id))
    form = FormUser()
    context = {
        "form": form
    }

    return render(request, "gallery/register.html", context)

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
