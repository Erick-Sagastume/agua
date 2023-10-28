from Cobros import views
from django.urls import path

urlpatterns = [
    path('',views.cobros,name="Cobros"),
    path('buscar/',views.buscador,name="Buscar"),
    path('nuevocobro/<str:id>',views.nuevo,name="NuevoCobro"),
    path('lista',views.lista,name="ListaCobros"),

]
