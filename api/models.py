from django.db import models

# Create your models here.


class chofer(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    
class ubicacion(models.Model):
    choferubi= models.ForeignKey(chofer,on_delete=models.CASCADE)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)