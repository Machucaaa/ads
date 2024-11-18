from django.db import models
from django.contrib.auth.models import AbstractUser

#from catalogo.models import Producto
# Create your models here.

class Propietario(AbstractUser):
    esta_activo = models.BooleanField(default=False)
    plan = models.IntegerField(default=365)
    fin_de_plan = models.DateField(auto_now=False,null=True)
    url = models.URLField(max_length=200) 
    whatsapp = models.CharField(max_length=15, null=True, blank=True)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Propietario, null=True, blank=True, on_delete=models.CASCADE)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    password= models.CharField(max_length=65, null=True, blank=True)
    device=models.CharField(max_length=50, null=True, blank=True)
    activo=models.BooleanField(default=True, null=True, blank=True)
    whatsappa = models.CharField(max_length=12, null=True, blank=True )

    def __str__(self):
        if self.nombre:
            nombre=self.nombre
        else:
            nombre=self.device

        return str(nombre)

