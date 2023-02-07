from django.shortcuts import render
from django.http import HttpResponse
from AppPre3.models import *
from AppPre3.forms import *

# Create your views here.

def inicio(request):
    return render(request,"AppPre3/inicio.html")

def Usuario(request):
    return render(request,"AppPre3/usuario.html")

def Venta(request):
    return render(request,"AppPre3/venta.html")
    
def Compra(request):
    return render(request,"AppPre3/compra.html")   


#FORMULARIOS


def form_User(request):
    if request.method=="POST":
        formularioUser=usuario_Formu(request.POST)
        if formularioUser.is_valid():
            infou=formularioUser.cleaned_data
            user=usuario(nombre=infou['nombre_usuario'],DNI=infou['DNI_usuario'],email=infou['email_usuario'],pais=infou['pais_usuario'])
            user.save()
            return render(request, "AppPre3/inicio.html")
    else:
        formularioUser=usuario_Formu()
    return render(request, "AppPre3/formu_User.html", {"formUser":formularioUser})


def form_Venta(request):
    if request.method=="POST":
        formularioVenta=venta_Formu(request.POST)
        if formularioVenta.is_valid():
            info=formularioVenta.cleaned_data
            sell=venta(nombreVenta=info["nombre_Venta"], fechaVenta=info["fecha_Venta"], montoVenta=info["monto_Venta"])
            sell.save()
            return render(request, "AppPre3/inicio.html")
    else:
        formularioVenta=venta_Formu()
    return render(request, "AppPre3/formu_Venta.html", {"formVenta":formularioVenta})    


def form_Compra(request):
    if request.method=="POST":
        formularioCompra=compra_Formu(request.POST)
        if formularioCompra.is_valid():
            info=formularioCompra.cleaned_data
            buy=compra(nombreCompra=info["nombre_Compra"], fechaCompra=info["fecha_Compra"], montoCompra=info["monto_Compra"])
            buy.save()
            return render(request, "AppPre3/inicio.html")
    else:
        formularioCompra=compra_Formu()
    return render(request, "AppPre3/formu_Compra.html", {"formCompra":formularioCompra})



    #BUSQUEDA

def busquedaCompra(request):
    return render(request, "AppPre3/busq_Compra.html")

def busquedaVenta(request):
    return render(request, "AppPre3/busq_Venta.html")   


def resultadoCompra(request):
    if request.GET["compra"]:
        busqueda=request.GET["compra"]
        resul=compra.objects.filter(nombreCompra__icontains=busqueda)
        return render(request, "AppPre3/resul_Compra.html", {"resultado":resul,"objeto":busqueda})
    else:
        respuesta="No enviaste datos"
    return HttpResponse(respuesta)


def resultadoVenta(request):
    if request.GET["venta"]:
        busqueda=request.GET["venta"]
        resul=venta.objects.filter(nombreVenta__icontains=busqueda)
        return render(request, "AppPre3/resul_Venta.html", {"resultado":resul,"objeto":busqueda})
    else:
        respuesta="No enviaste datos"
    return HttpResponse(respuesta)



    #ACTUALIZAR DATOS
