from django import forms
from .models import Servicio

ACTIVO = (
    ('True','Activo'),
    ('False','Baja'),
)

class ServicioForm(forms.ModelForm):
   
    class Meta:
        model = Servicio
        fields = ['nombre','limite','mensual','estado']

        widgets = {        
            'nombre': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),
            'limite': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),
            'mensual': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),
            'estado': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),
           
        }

