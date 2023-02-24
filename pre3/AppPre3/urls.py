from django.urls import path
from AppPre3.views import *
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path("", inicio, name="Inicio"),

    #path para login logout editar y registro
    path("login/", inicio_sesion, name="Login"),
    path("register/", registro, name="Registro"),
    path("logout/", LogoutView.as_view(template_name="AppPre3/logout.html"), name="Logout"),
    path("editar/", Editar_Usuario, name="Editar User"),
    path("avatar/", add_avatar, name="Add Avatar"),
    path ("about/",about ,name="About"),

    # path 3era preentrega
    path("compra/", Compra, name="Compra"),
    path("venta/", Venta, name="Venta"),
    path("formulario_User/", form_User, name="Formulario Usuario"),
    path("formulario_Venta/", form_Venta, name="Formulario Venta"),
    path("formulario_Compra/", form_Compra, name="Formulario Compra"),
    path("busque_Compra/", busquedaCompra, name="Busqueda Compra"),
    path("resul_Compra/", resultadoCompra, name="Resultado Compra"),
    path("busque_Venta/", busquedaVenta, name="Busqueda Venta"),
    path("resul_Venta/", resultadoVenta, name="Resultado Venta"),
    
    
    #CRUDs usuario 3era preentrega
    path("leerUsuarios/", leer_usuarios, name="Leer Usuarios"),
    path("eliminarUsuarios/<user_name>/", eliminar_usuario, name="Eliminar Usuario"),
    path("editarUsuarios/<user_name>/", Editar_Usuario, name="Editar Usuario"),


    #CRUDs de ventas

    path("venta/list",ListaVenta.as_view(),name="Leer Venta"),
    path("venta/<int:pk>",DetalleVenta.as_view(),name="Detalle Venta"),
    path("venta/crear/",CrearVenta.as_view(),name="Crear Venta"),
    path("venta/editar/<int:pk>",ActualizarVenta.as_view(),name="Editar Venta"),
    path("venta/borrar/<int:pk>",BorrarVenta.as_view(),name="Borrar Venta"),
]