from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    dpi = models.BigIntegerField(blank=True,null=True,default=0)
    rol = models.CharField(max_length=250,null=True,blank=True)
    estado = models.IntegerField(blank=False,null=False,default=0)
    