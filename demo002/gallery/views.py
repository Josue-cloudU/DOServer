from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import generic
from django.urls import reverse_lazy

from .serializers import UserSerializer, ItemNewSerializer, ItemSerializer, UserListSerializer, ItemCatSerializer

from .forms import FormUser, FormItem
import requests

from gallery.models import Item
from .models import User
# Create your views here.

class Index(generic.TemplateView):
    template_name = "gallery/index.html"

#-----------------------------------------------------------------------------------------------------------

def createItem(request):
    form = FormItem(request.POST)
    if request.method=='POST':
        form = FormItem(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            user_update = form.cleaned_data['user_update']
            status = form.cleaned_data['status']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            url = "http://localhost:8000/item_create/"
            payload = {
                "user": user_id,
                "user_update": user_update,
                "status": status,
                "category": category,
                "description": description

            }
            response = requests.post(url, data=payload)
            return redirect('gallery:index')
            #print("User: {0}".format(user_id))
    form = FormItem()
    context = {
        "form": form
    }

    return render(request, "gallery/new_item.html", context)

class ItemCreate(generics.CreateAPIView):
    serializer_class = ItemSerializer

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

def list_Item(request):
    url = "http://localhost:8000/list_new_item/"
    response = requests.get(url)
    obj = response.json()
    context = {
        "objs":obj
    }
    return render(request, "gallery/list_item.html", context)

class ListNewItem(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemNewSerializer

def list_AAItem(request):
    url = "http://localhost:8000/list_aaitem/"
    response = requests.get(url)
    obj = response.json()
    context = {
        "objs":obj
    }
    return render(request, "gallery/list_aaitem.html", context)

class ListAAItem(generics.ListCreateAPIView):
    queryset = Item.objects.filter(category=3)
    serializer_class = ItemCatSerializer

def list_SRItem(request):
    url = "http://localhost:8000/list_sritem/"
    response = requests.get(url)
    obj = response.json()
    context = {
        "objs":obj
    }
    return render(request, "gallery/list_sritem.html", context)

class ListSRItem(generics.ListCreateAPIView):
    queryset = Item.objects.filter(category=2)
    serializer_class = ItemCatSerializer

def list_RItem(request):
    url = "http://localhost:8000/list_ritem/"
    response = requests.get(url)
    obj = response.json()
    context = {
        "objs":obj
    }
    return render(request, "gallery/list_ritem.html", context)

class ListRItem(generics.ListCreateAPIView):
    queryset = Item.objects.filter(category=1)
    serializer_class = ItemCatSerializer

def list_User(request):
    url = "http://localhost:8000/list_user/"
    response = requests.get(url)
    obj = response.json()
    context = {
        "objs":obj
    }
    return render(request, "gallery/list_user.html", context)

class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
