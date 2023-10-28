from django import forms
from .models import Lectura

ACTIVO = (
    ('True','Activo'),
    ('False','Baja'),
)

class LecturaForm(forms.ModelForm):
   
    class Meta:
        model = Lectura
        fields = ['id_cuenta','anterior','actual','mes']

        widgets = {  
            'id_cuenta': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','readonly':True,'require':True}),      
            'anterior': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),
            'actual': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),
            'mes': forms.TextInput(attrs={'class': 'form-control','style':'border: 1px solid black','require':True}),
           
        }

