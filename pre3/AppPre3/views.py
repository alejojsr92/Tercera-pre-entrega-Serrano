from django.shortcuts import render
from django.http import HttpResponse
from AppPre3.models import *
from AppPre3.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


def inicio_sesion(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            log=authenticate(username=user,password=contra)
            if log:
                login(request,log)
                return render(request, "AppPre3/inicio.html", {"mensaje":f"Bienvenido {log}"})
        else:
            return render(request, "AppPre3/inicio.html", {"mensaje":"Datos Incorrectos"})
    else:
        form=AuthenticationForm()
    return render(request, "AppPre3/login.html", {"formulario":form})



def registro(request):
    if request.method=="POST":
        form=RegistroUsuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request, "AppPre3/registrohecho.html", {"mensaje":"Usuario Creado"})
    else:
        form=RegistroUsuario()
    return render(request, "AppPre3/registro.html", {"formulario":form})


@login_required
def Editar_Usuario(request):
    user=request.user
    if request.method=="POST":
        form=editarUser(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user.email=info["email"]
            user.set_password=(info["password1"])
            user.first_name=info["first_name"]
            user.last_name=info["last_name"]
            user.save()
            return render(request, "AppPre3/inicio.html")
    else:
        form=editarUser(initial={"email":user.email,"first_name":user.first_name,"last_name":user.last_name,})
    
    return render(request, "AppPre3/EditarPerfil.html", {"formulario":form, "usuario":user})

@login_required
def add_avatar(request):
    if request.method=="POST":
        form=AvatarFormu(request.POST, request.FILES)
        if form.is_valid():
            usuarioActual= User.objects.get(username=request.user)
            avatar=Avatar(user=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar.save()
            return render(request, "AppPre3/inicio.html")
    else:
        form=AvatarFormu()

    return render(request, "AppPre3/addAvatar.html", {"formulario":form})
        



def inicio(request):
    return render(request,"AppPre3/inicio.html")
def about(request):
    return render(request,"AppPre3/about.html")
@login_required
def Usuario(request):
    return render(request,"AppPre3/usuario.html")
@login_required
def Venta(request):
    return render(request,"AppPre3/venta.html")
@login_required
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

@login_required
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

@login_required
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
@login_required
def busquedaCompra(request):
    return render(request, "AppPre3/busq_Compra.html")

@login_required
def busquedaVenta(request):
    return render(request, "AppPre3/busq_Venta.html")   

@login_required
def resultadoCompra(request):
    if request.GET["compra"]:
        busqueda=request.GET["compra"]
        resul=compra.objects.filter(nombreCompra__icontains=busqueda)
        return render(request, "AppPre3/resul_Compra.html", {"resultado":resul,"objeto":busqueda})
    else:
        respuesta="No enviaste datos"
    return render(request, "AppPre3/resul_Compra.html", {"mensaje":respuesta})

@login_required
def resultadoVenta(request):
    if request.GET["venta"]:
        busqueda=request.GET["venta"]
        resul=venta.objects.filter(nombreVenta__icontains=busqueda)
        return render(request, "AppPre3/resul_Venta.html", {"resultado":resul,"objeto":busqueda})
    else:
        respuesta="No enviaste datos"
    return HttpResponse(respuesta)



    #CRUD USUARIO 3era preentrega

@login_required
def leer_usuarios(request):
    user=usuario.objects.all()
    return render(request, "AppPre3/leer_usuarios.html", {"datos":user})

@login_required
def eliminar_usuario(request, user_name):
    user=usuario.objects.get(nombre=user_name)
    user.delete()
    usuarios=usuario.objects.all()
    return render(request, "AppPre3/leer_usuarios.html",{"datos":usuarios})

@login_required
def editar_usuario(request, user_name):
    user=usuario.objects.get(nombre=user_name)
    if request.method=="POST":
        formularioUser=usuario_Formu(request.POST)
        if formularioUser.is_valid():
            infou=formularioUser.cleaned_data
            user.nombre=infou["nombre_usuario"]
            user.DNI=infou["DNI_usuario"]
            user.email=infou["email_usuario"]
            user.pais=infou["pais_usuario"]
            user.save()
            return render(request, "AppPre3/inicio.html")
    else:
        formularioUser=usuario_Formu(initial={"nombre_usuario":user.nombre, "DNI_usuario":user.DNI, "email_usuario":user.email, "pais_usuario":user.pais})
    return render(request, "AppPre3/editar_usuario.html", {"formUser":formularioUser, "nombre_usuario":user_name})



class ListaVenta(LoginRequiredMixin, ListView):
    model= venta

class DetalleVenta(LoginRequiredMixin, DetailView):
    model=venta

class CrearVenta(LoginRequiredMixin, CreateView):
    model=venta
    success_url="/AppPre3/venta/list"
    fields=["nombreVenta","fechaVenta","montoVenta"]

class ActualizarVenta(LoginRequiredMixin, UpdateView):
    model=venta
    success_url="/AppPre3/venta/list"
    fields=["nombreVenta","fechaVenta","montoVenta"]


class BorrarVenta(LoginRequiredMixin, DeleteView):
    model=venta
    success_url="/AppPre3/venta/list"
    