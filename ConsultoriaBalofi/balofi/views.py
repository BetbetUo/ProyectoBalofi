from django.shortcuts import render, get_object_or_404, redirect
from .models import Clientes, Productos, Facturas
from .forms import FormCliente, FormProducto, FormFactura
from django.http import HttpResponse



# Create your views here.
def Home(request):
	clientes = Clientes.objects.all()
	return render(request, 'balofi/Home.html',{'clientes':clientes})

def editar(request, pk):
	cliente = get_object_or_404(Clientes, pk=pk)
	if request.method == "POST":
		form = FormCliente(request.POST,instance=cliente)
		if form.is_valid():
			x = form.save(commit=False)
			cliente.save()
			return redirect(Home)
	else:
		form = FormCliente(instance = cliente)
		return render(request,'balofi/editar.html',{'form':form})
	form=FormCliente(instance = cliente)
	return render(request, 'balofi/editar.html', {'form':form})
	
def consultar(request, pk):
	x = get_object_or_404(Clientes, pk=pk)
	clientes = Clientes.objects.filter(rfc=x.rfc)
	return render(request, 'balofi/consultar.html', {'clientes':clientes})

def registrar(request):
	if request.method == "POST":
		form = FormCliente(request.POST)
		if form.is_valid():
			cliente = form.save(commit=False)
			cliente.save()
			return redirect(Home)
	else:
		form=FormCliente()
	return render(request,'balofi/registrar.html',{'form':form})
	#return render(request, 'balofi/registrar.html', {})
	

def VerProductos(request, pk):
	x = get_object_or_404(Clientes, pk=pk)
	productos = Productos.objects.filter(cliente=x.rfc)
	return render(request, 'balofi/productos.html', {'productos':productos, 'clientes':x})
		
def editar_Producto(request, pk, rfc):
	producto = get_object_or_404(Productos, pk=pk)
	cliente = get_object_or_404(Clientes, rfc=rfc)
	if request.method == "POST":
		form = FormProducto(request.POST,instance=producto)
		if form.is_valid():
			x = form.save(commit=False)
			producto.save()
			return redirect(VerProductos, cliente.rfc)
	else:
		form = FormProducto(instance = producto)
		return render(request,'balofi/editarProducto.html',{'form':form, 'cliente':cliente})
	form=Formproducto(instance = producto)
	return render(request, 'balofi/editarProducto.html', {'form':form, 'cliente':cliente})
	
def consultar_Producto(request, pk, rfc):
	x = get_object_or_404(Productos, pk=pk)
	y = get_object_or_404(Clientes, rfc=rfc)
	productos = Productos.objects.filter(idProducto=x.idProducto)
	return render(request, 'balofi/consultarProducto.html', {'productos':productos, 'cliente':y})
	
def registrar_Producto(request, pk):
	x = get_object_or_404(Clientes, pk=pk)
	if request.method == "POST":
		form = FormProducto(request.POST)
		if form.is_valid():
			producto = form.save(commit=False)
			producto.cliente = x.rfc
			producto.save()
			return redirect(VerProductos, x.rfc)
	else:
		form=FormProducto()
	return render(request,'balofi/registrarProducto.html',{'form':form, 'cliente':x})
	

def VerFacturas(request, pk):
	x = get_object_or_404(Clientes, pk=pk)
	facturas = Facturas.objects.filter(cliente=x.rfc)
	return render(request, 'balofi/facturas.html', {'facturas':facturas, 'clientes':x})
	
def editar_Factura(request, pk, rfc):
	factura = get_object_or_404(Facturas, pk=pk)
	cliente = get_object_or_404(Clientes, rfc=rfc)
	if request.method == "POST":
		form = FormFactura(request.POST,instance=factura)
		if form.is_valid():
			x = form.save(commit=False)
			factura.save()
			return redirect(VerFacturas, cliente.rfc)
	else:
		form = FormFactura(instance = factura)
		return render(request,'balofi/editarFactura.html',{'form':form, 'cliente':cliente})
	form=FormFactura(instance = factura)
	return render(request, 'balofi/editarFactura.html', {'form':form, 'cliente':cliente})
	
def consultar_Factura(request, pk, rfc):
	x = get_object_or_404(Facturas, pk=pk)
	y = get_object_or_404(Clientes, rfc=rfc)
	facturas = Facturas.objects.filter(idFactura=x.idFactura)
	return render(request, 'balofi/consultarFactura.html', {'facturas':facturas, 'cliente':y})
	
def registrar_Factura(request, pk):
	x = get_object_or_404(Clientes, pk=pk)
	if request.method == "POST":
		form = FormFactura(request.POST)
		if form.is_valid():
			factura = form.save(commit=False)
			factura.cliente = x.rfc
			factura.save()
			return redirect(VerFacturas, x.rfc)
	else:
		form=FormFactura()
	return render(request,'balofi/registrarFactura.html',{'form':form, 'cliente':x})