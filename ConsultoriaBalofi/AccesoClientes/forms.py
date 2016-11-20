from django import forms
from balofi.models import Clientes


class FormCliente(forms.Form):
	rfc = forms.CharField(max_length=13)
	password = forms.CharField(widget=forms.PasswordInput())
	widgets = {'password': forms.PasswordInput(),}