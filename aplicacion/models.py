from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()

class Frutas(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)
    
class Verduras(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)

class Ganado(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)
