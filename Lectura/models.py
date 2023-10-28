from django.db import models
from user.models import User
from Cliente.models import Cuenta
import uuid

class Lectura(models.Model):
    id_cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,blank=False,null=False)
    anterior = models.DecimalField(max_digits=12,decimal_places=2,blank=False,null=False,default=0.00)
    actual = models.DecimalField(max_digits=12,decimal_places=2,blank=False,null=False,default=0.00)
    consumo = models.DecimalField(max_digits=12,decimal_places=2,blank=False,null=False,default=0.00)
    exceso = models.DecimalField(max_digits=12,decimal_places=2,blank=False,null=False,default=0.00)
    cargo_mes = models.DecimalField(max_digits=12,decimal_places=2,blank=False,null=False,default=0.00)
    cargo_exceso = models.DecimalField(max_digits=12,decimal_places=2,blank=False,null=False,default=0.00)
    cargo_total = models.DecimalField(max_digits=12,decimal_places=2,blank=False,null=False,default=0.00)
    mes = models.CharField(max_length=250,blank=False,null=False,default='No Asignado')
    ciclo = models.IntegerField(blank=False,null=False,default=0)
    fecha = models.DateTimeField(blank=False,null=False)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    estado = models.IntegerField(blank=False,null=False,default=0)

    class Meta:
        ordering = ["-id_cuenta"]

    def __str__(self):
        return str(self.id_cuenta)