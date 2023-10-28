from Lectura import views
from django.urls import path

urlpatterns = [
    path('',views.lectura,name="Lectura"),
    path('buscar2/',views.buscador2,name="Buscar2"),
    path('nuevalectura/<str:cuenta>',views.nuevalectura,name="NuevaLectura"),
    path('actualizalectura/<str:id>',views.actualizalectura,name="ActualizaLectura"),
]
