from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppPre3.models import Avatar


class usuario_Formu(forms.Form):
    nombre_usuario=forms.CharField()
    DNI_usuario=forms.IntegerField()
    email_usuario=forms.EmailField()
    pais_usuario=forms.CharField()

class venta_Formu(forms.Form):
    nombre_Venta=forms.CharField()
    fecha_Venta=forms.DateField()
    monto_Venta=forms.IntegerField()

class compra_Formu(forms.Form):
    nombre_Compra=forms.CharField()
    fecha_Compra=forms.DateField()
    monto_Compra=forms.IntegerField()


class RegistroUsuario(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ["username", "email", "first_name", "last_name", "password1", "password2"]



class editarUser(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ["email", "first_name", "last_name", "password1", "password2"]


class AvatarFormu(forms.ModelForm):
    class Meta:
        model= Avatar
        fields=["imagen"]

