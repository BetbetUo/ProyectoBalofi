from django.shortcuts import render, get_object_or_404, redirect
from balofi.models import Clientes, Productos, Facturas
from .forms import FormCliente
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def ClientesBalofi(request):
	if request.method == 'GET':
		form = FormCliente()
	else:
		form = FormCliente(request.POST)
		if form.is_valid():
			cliente_rfc = form.cleaned_data['rfc']
			password = form.cleaned_data['password']
			try:
				x = Clientes.objects.get(rfc=cliente_rfc)
				if password == x.password:
					return redirect(consultar, x.rfc)
				else:
					return render(request, 'AccesoClientes/login.html', {'form':form, 'invalidPass':True})
			except Clientes.DoesNotExist:
				return render(request, 'AccesoClientes/login.html', {'form':form, 'invalidUsr':True})
	return render(request, 'AccesoClientes/login.html', {'form':form})
	
def consultar(request, pk):
	x = get_object_or_404(Clientes, pk=pk)
	clientes = Clientes.objects.filter(rfc=x.rfc)
	return render(request, 'AccesoClientes/consultar.html', {'clientes':clientes})
	
def VerProductos(request, pk):
	x = get_object_or_404(Clientes, pk=pk)
	productos = Productos.objects.filter(cliente=x.rfc)
	return render(request, 'AccesoClientes/productos.html', {'productos':productos, 'clientes':x})
	
def consultar_Producto(request, pk, rfc):
	x = get_object_or_404(Productos, pk=pk)
	y = get_object_or_404(Clientes, rfc=rfc)
	productos = Productos.objects.filter(idProducto=x.idProducto)
	return render(request, 'balofi/consultarProducto.html', {'productos':productos, 'cliente':y})
	
	
def VerFacturas(request, pk):
	x = get_object_or_404(Clientes, pk=pk)
	facturas = Facturas.objects.filter(cliente=x.rfc)
	return render(request, 'AccesoClientes/facturas.html', {'facturas':facturas, 'clientes':x})
	
def consultar_Factura(request, pk, rfc):
	x = get_object_or_404(Facturas, pk=pk)
	y = get_object_or_404(Clientes, rfc=rfc)
	facturas = Facturas.objects.filter(idFactura=x.idFactura)
	return render(request, 'AccesoClientes/consultarFactura.html', {'facturas':facturas, 'cliente':y})