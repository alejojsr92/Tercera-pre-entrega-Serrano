from django import forms

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