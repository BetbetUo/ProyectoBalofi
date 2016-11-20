from django import forms
from .models import Clientes, Productos, Facturas


class FormCliente(forms.ModelForm):
	class Meta:
		model=Clientes
		fields=('rfc','password','nombre','aPaterno','aMaterno','direccion','telefono','correo','razonSocial','giro',)
		
class FormProducto(forms.ModelForm):
	class Meta:
		model=Productos
		fields=('nombre','marca','color','tamanio','numeroDePiezas','entradaOSalida','fechaMovimiento','caducidad',)
		
class FormFactura(forms.ModelForm):
	class Meta:
		model=Facturas
		fields=('rfcEmisor','nombreEmisor','direccionEmisor','fecha','rfcReceptor','nombreReceptor','direccionReceptor','tipo','subtotal','IVA','total')
		