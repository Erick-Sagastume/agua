from django import forms
from .models import Cliente,Cuenta,Servicio

ACTIVO = (
    ('True','Activo'),
    ('False','Baja'),
)

SERVICIO = [(c.id_servicio,c.nombre) for c in Servicio.objects.all()]

class ClienteForm(forms.ModelForm):
   
    class Meta:
        model = Cliente
        fields = ['dpi','nombre','apellido','direccion','estado']

        widgets = {  
            'dpi': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),      
            'nombre': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),
            'apellido': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),
            'estado': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),
           
        }

class CuentaForm(forms.ModelForm):
   
    class Meta:
        model = Cuenta
        fields = ['id_cuenta','dpi','servicio','direccion']

        widgets = {  
            'id_cuenta': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','readonly':True,'require':True,}),  
            'dpi': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','readonly':True,'require':True}),      
            'servicio':forms.Select(attrs={'class': 'selectpicker form-control','data-style':'btn-outline-info','style':'border: 1px solid black','type':'checkbox','require':False},choices=SERVICIO),
            'direccion': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),

           
        }