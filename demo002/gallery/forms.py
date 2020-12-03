from django import forms
from .models import Item

class FormItem(forms.Form):
    user_id = forms.CharField()
    user_update = forms.CharField()
    status = forms.BooleanField()
    category= forms.CharField()
    description = forms.CharField(max_length=128)

class FormUser(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
