from django import forms
from .models import Cundina

class FormSaving(forms.Form):
    user_id = forms.CharField()
    user_update = forms.CharField()
    status = forms.BooleanField()
    descripcion = forms.CharField(max_length=128)
    cantahorro = forms.CharField()
    nparticipantes = forms.CharField()

class FormUser(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
