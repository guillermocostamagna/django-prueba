from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return {self.nombre}
    
class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null = True, blank=True)
    pais_origen = models.ForeignKey(Pais,on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return f'{self.apellido, self.nombre}'