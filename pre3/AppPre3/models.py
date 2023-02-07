from django.db import models

# Create your models here.


class usuario(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} ---- DNI: {self.DNI} ---- email: {self.email} ---- pais: {self.pais}"

    nombre=models.CharField(max_length=30)
    DNI=models.IntegerField()
    email=models.EmailField()
    pais=models.CharField(max_length=15)

class venta(models.Model):
    nombreVenta=models.CharField(max_length=30)
    fechaVenta=models.DateField()
    montoVenta=models.IntegerField()

class compra(models.Model):
    nombreCompra=models.CharField(max_length=30)
    fechaCompra=models.DateField()
    montoCompra=models.IntegerField()

