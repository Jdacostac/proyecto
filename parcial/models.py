from django.db import models

# Create your models here.
class comensal(models.Model):
    cedula = models.IntegerField(max_length=100)
    nombre = models.CharField(max_length=60)
class menu(models.Model):
    id_menu= models.IntegerField(max_length=100)
    tipo_comida = models.CharField(max_length=60)
class pedido(models.Model):
    id_pedido = models.IntegerField(max_length=100)
    plato = models.CharField(max_length=60)
class mesero(models.Model):
    id_mesero = models.IntegerField(max_length=100)
    nombre = models.CharField(max_length=60)
class entrega(models.Model):
    id_entrega = models.IntegerField(max_length=100)
    tipo_entrega = models.CharField(max_length=60)
class cocinero(models.Model):
    id_cocinero = models.IntegerField(max_length=100)
    nombre = models.CharField(max_length=60)
class prerara(models.Model):
    id_preparacion = models.IntegerField(max_length=100)
    receta = models.CharField(max_length=60)
class comida(models.Model):
    id_comida = models.IntegerField(max_length=100)
    nombre_platillo = models.CharField(max_length=60)
class contiene(models.Model):
    id_contiene = models.IntegerField(max_length=100)
    tipo= models.CharField(max_length=60)  
class ingredientes(models.Model):
    id_ingredientes = models.IntegerField(max_length=100)
    tipo_ingredientes = models.CharField(max_length=60)
class inventario(models.Model):
    id_inventario= models.IntegerField(max_length=100)
    procedencia_ingredientes= models.CharField(max_length=60)
  