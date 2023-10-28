from django.db import models
from user.models import User
from Servicios.models import Servicio
import uuid

class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key=True,blank=False,null=False)
    dpi = models.BigIntegerField(blank=False,null=False)
    nombre = models.CharField(max_length=250,blank=False,null=False)
    apellido = models.CharField(max_length=350,blank=False,null=False)
    direccion = models.CharField(max_length=750,blank=False,null=False)
    telefono = models.CharField(max_length=8,blank=False,null=False)
    correo = models.CharField(max_length=250,blank=True,null=True,default='S/C')
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    fecha = models.DateTimeField(blank=False,null=False)
    estado = models.IntegerField(blank=False,null=False,default=1)

    class Meta:
        ordering = ["-apellido"]

    def __str__(self):
        return str(self.dpi)
    

class Cuenta(models.Model):
    id_cuenta = models.CharField(max_length=150,primary_key=True,blank=False,null=False)
    dpi = models.ForeignKey(Cliente,on_delete=models.CASCADE,blank=False,null=False)
    servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE,blank=False,null=False)
    direccion = models.CharField(max_length=750,blank=False,null=False)
    fecha = models.DateTimeField(blank=False,null=False)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    estado = models.IntegerField(blank=False,null=False,default=1)

    class Meta:
        ordering = ["-id_cuenta"]

    def __str__(self):
        return str(self.id_cuenta)
    
