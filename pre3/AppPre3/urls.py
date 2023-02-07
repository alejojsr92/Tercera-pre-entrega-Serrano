from django.urls import path
from AppPre3.views import *

urlpatterns=[
    path("", inicio, name="Inicio"),
    path("compra/", Compra, name="Compra"),
    path("venta/", Venta, name="Venta"),
    path("formulario_User/", form_User, name="Formulario Usuario"),
    path("formulario_Venta/", form_Venta, name="Formulario Venta"),
    path("formulario_Compra/", form_Compra, name="Formulario Compra"),
    path("busque_Compra/", busquedaCompra, name="Busqueda Compra"),
    path("resul_Compra/", resultadoCompra, name="Resultado Compra"),
    path("busque_Venta/", busquedaVenta, name="Busqueda Venta"),
    path("resul_Venta/", resultadoVenta, name="Resultado Venta"),
]