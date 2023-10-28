from django.db import models
from user.models import User

class Servicio(models.Model):
    id_servicio = models.BigAutoField(primary_key=True,blank=False,null=False)
    nombre = models.CharField(max_length=750,blank=False,null=False)
    limite = models.IntegerField(blank=False,null=False,default=0)
    mensual = models.DecimalField(max_digits=12,decimal_places=2,blank=False,null=False,default=0.00)
    fecha = models.DateTimeField(blank=False,null=False)
    estado = models.IntegerField(blank=False,null=False,default=1)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)

    class Meta:
        ordering = ["id_servicio"]

    def __str__(self):
        return str(self.nombre)

