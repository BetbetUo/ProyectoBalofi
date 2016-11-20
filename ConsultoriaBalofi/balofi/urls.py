from django.conf.urls import include,url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^home$', views.Home, name='Home'),
	url(r'^cliente/(.+)$', views.editar, name='cliente'),
	url(r'^consulta/(.+)$', views.consultar, name='consulta'),
	url(r'^registro$', views.registrar, name='registro'),
	url(r'^productos/(.+)$', views.VerProductos, name='productos'),
	url(r'^editarProducto/(?P<pk>.+)/(?P<rfc>.+)$', views.editar_Producto, name='editarProducto'),
	url(r'^consultaProducto/(?P<pk>.+)/(?P<rfc>.+)$', views.consultar_Producto, name='consultaProducto'),
	url(r'^registroProducto/(.+)$', views.registrar_Producto, name='registroProducto'),
	url(r'^facturas/(.+)$', views.VerFacturas, name='facturas'),
	url(r'^editarFactura/(?P<pk>.+)/(?P<rfc>.+)$', views.editar_Factura, name='editarFactura'),
	url(r'^consultaFactura/(?P<pk>.+)/(?P<rfc>.+)$', views.consultar_Factura, name='consultaFactura'),
	url(r'^registroFactura/(.+)$', views.registrar_Factura, name='registroFactura'),
]
