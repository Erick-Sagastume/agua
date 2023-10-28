from Cliente import views
from django.urls import path

urlpatterns = [
    path('',views.cliente,name="Cliente"),
    path('nuevocliente/',views.nuevo,name="NuevoCliente"),
    path('cuentas',views.cuenta,name="Cuenta"),
    path('detalleservicioscliente/<int:id>',views.detalleservicios,name="DetalleServicioCliente"),
    path('detallepagoscliente/<str:id>',views.detallepagoscliente,name="DetallePagosCliente"),
    path('cuentas2',views.cuenta2,name="Cuenta2"),
    path('nuevacuenta/',views.nuevacuenta,name="NuevaCuenta"),
    path('eliminarasociado/<int:id>',views.eliminar,name='EliminarAsociado'),
    path('actualizarcliente/<str:id>',views.actualizarcliente,name="ActualizarCliente"),
    path('actualizacuenta/<str:id>',views.actualizacuenta,name="ActualizaCuenta"),
    path('darbajacuenta/<str:cuenta>',views.bajacuenta,name='BajaCuenta'),
    path('daraltacuenta/<str:cuenta>',views.altacuenta,name='AltaCuenta'),
    path('darbajacliente/<int:dpi>',views.bajacliente,name='BajaCliente'),
    path('daraltacliente/<int:dpi>',views.altacliente,name='AltaCliente'),
    path('listacliente/',views.listacliente,name="ListaCliente"),
    path('listacliente2/',views.listacliente2,name="ListaCliente2"),
    path('pdf/<str:id>',views.pdf,name='PDF'),
    path('pdf2/<str:id>/<str:mes>',views.pdf2,name='PDF2'),

]
