from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Propietario, Cliente
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Propietario
        fields = "__all__"

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'nombre de usuario?'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'email?'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'password?'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'confirmar password'}))
    class Meta:
        model = Propietario
        fields = ['username', 'email', 'password1', 'password2']       

class ClienteForm(ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'tu nombre?'}))
    whatsapp = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'tu whatsapp?'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'password?'}))    
    whatsappa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2 link_whats', 'placeholder':'whatsapp destino?'}))
    class Meta:
        model = Cliente
        fields = ['nombre', 'whatsapp','device', 'proveedor', 'password', 'whatsappa']               

class LoginClienteForm(ModelForm):

    whatsapp = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'tu whatsapp?'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'password?'}))    

    
    class Meta:
        model = Cliente
        fields = [ 'whatsapp',  'password']                       