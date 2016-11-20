from django.conf.urls import include,url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^ClientesBalofi$', views.ClientesBalofi, name='ClientesBalofi'),
	url(r'^ClientesBalofi/consulta/(.+)$', views.consultar, name='consulta'),
	url(r'^ClientesBalofi/productos/(.+)$', views.VerProductos, name='productos'),
	url(r'^ClientesBalofi/facturas/(.+)$', views.VerFacturas, name='facturas'),
	url(r'^ClientesBalofi/consultaProducto/(?P<pk>.+)/(?P<rfc>.+)$', views.consultar_Producto, name='consultaProducto'),
	url(r'^ClientesBalofi/consultaFactura/(?P<pk>.+)/(?P<rfc>.+)$', views.consultar_Factura, name='consultaFactura'),
]
