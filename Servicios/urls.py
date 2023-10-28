from Servicios import views
from django.urls import path

urlpatterns = [
    path('listaservicios/',views.lista,name="ListaServicio"),
    path('listaservicios2/',views.lista2,name="ListaServicio2"),
    path('nuevoservicio/',views.nuevo,name="NuevoServicio"),
    #path('nuevocliente/',views.nuevo,name="NuevoCliente"),
    path('actualizar/<str:id>',views.actualizar,name="Actualizar"),
    path('eliminarservicio/<int:id>', views.eliminarservicio, name="EliminarServicio"),
    path('darbajaservicio/<int:id>',views.bajaservicio,name='BajaServicio'),
    path('daraltaservicio/<int:id>',views.altaservicio,name='AltaServicio'),
]
