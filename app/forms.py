import datetime
from django import forms
from app.models import Staff, Project, Product

class StaffForm(forms.Form):

    name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    position = forms.CharField(label='Cargo')
    rank = forms.IntegerField(label='Rango')
    since = forms.DateField(
        label='Ingreso',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    email = forms.EmailField(label='Correo')


class ProjectForm(forms.Form):

    code = forms.IntegerField(label='Codigo')
    title = forms.CharField(label='Título')
    start = forms.DateField(
        label='Inicio',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    state = forms.CharField(label='Estado')


class ProductForm(forms.Form):
    
    serial = forms.IntegerField(label='Serie')
    product_name = forms.CharField(label='Objeto')
    availability = forms.BooleanField(label='Disponible', required=False)