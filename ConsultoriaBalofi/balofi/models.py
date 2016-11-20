from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Clientes(models.Model):
	rfc = models.CharField(max_length=13, primary_key=True)
	password = models.CharField(max_length=20)
	nombre = models.CharField(max_length=30)
	aPaterno = models.CharField(max_length=50)
	aMaterno = models.CharField(max_length=50)
	direccion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=10)
	correo = models.EmailField(max_length=50)
	razonSocial = models.CharField(max_length=50)
	giro = models.CharField(max_length=50)
	
class Productos(models.Model):
	idProducto = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	marca = models.CharField(max_length=50)
	color = models.CharField(max_length=15)
	tamanio = models.CharField(max_length=15)
	numeroDePiezas = models.IntegerField(default=1)
	entradaOSalida = models.IntegerField(default=0)
	fechaMovimiento = models.DateField(auto_now=False,auto_now_add=False)
	caducidad = models.DateField(auto_now=False,auto_now_add=False)
	cantidad = models.IntegerField(default=1)
	cliente = models.CharField(max_length=13)
	
class Facturas(models.Model):
	idFactura = models.AutoField(primary_key=True)
	rfcEmisor = models.CharField(max_length=13)
	nombreEmisor = models.CharField(max_length=50)
	direccionEmisor = models.CharField(max_length=100)
	fecha = models.DateField(auto_now=False,auto_now_add=False)
	rfcReceptor = models.CharField(max_length=13)
	nombreReceptor = models.CharField(max_length=50)
	direccionReceptor = models.CharField(max_length=100)
	tipo = models.IntegerField(default=0)
	subtotal = models.DecimalField(max_digits=10,decimal_places=4)
	IVA = models.DecimalField(max_digits=10,decimal_places=4)
	total = models.DecimalField(max_digits=10,decimal_places=4)
	cliente = models.CharField(max_length=13)
