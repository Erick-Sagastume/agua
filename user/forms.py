from django import forms
from django.forms import ModelForm
from user.models import User

ROL = (
('admin','Administrador'),
('fontanero','Fontanero'),
)
PANEL = (
    ('True','Si'),
    ('False','No'),
)
ACTIVO = (
    ('True','Activo'),
    ('False','Baja'),
)
SUPER = (
    ('True','Si'),
    ('False','No'),
)
class RegistroForm(ModelForm):

    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email','rol','is_staff','is_active','is_superuser']
        labels = {'username':'Nombre de Usuario','password':'Password','first_name':'Nombres','last_name':'Apellidos',
                 'email':'Correo Electronico','rol':'Rol de Sistema','is_staff':'Panel Admin','is_active':'Usuario Activo',
                 'is_superuser':'Es Super Usuario'}
        help_texts = {
            'username': None,
            'password':None,
            'is_staff':None,
            'is_active':None,
            'is_superuser':None,
        }         

        widgets = { 

                 'username':forms.TextInput(attrs={'style':'border: 1px solid black','class': 'form-control text-center','placeholder':'Nombre de Usuario','autofocus': True,'require':True}),
                 'password':forms.TextInput(attrs={'style':'border: 1px solid black','class': 'form-control text-center','placeholder':'Password','type': 'password','require':True}),
                 'first_name':forms.TextInput(attrs={'style':'border: 1px solid black','class': 'form-control text-center','placeholder':'Nombres','require':True}),
                 'last_name':forms.TextInput(attrs={'style':'border: 1px solid black','class': 'form-control text-center','placeholder':'Apellidos','require':True}), 
                 'email':forms.TextInput(attrs={'style':'border: 1px solid black','class': 'form-control text-center','placeholder':'correo@electronico.com','type':'email','require':True}),
                 'rol':forms.Select(attrs={'style':'border: 1px solid black','class': 'selectpicker form-control text-center','data-style':'btn-outline-info','placeholder':'Rol','require':True},choices=ROL), 
                 'is_staff':forms.Select(attrs={'style':'border: 1px solid black','class': 'selectpicker form-control text-center','data-style':'btn-outline-info','type':'checkbox','require':False},choices=PANEL),
                 'is_active':forms.Select(attrs={'style':'border: 1px solid black','class': 'selectpicker form-control text-center','data-style':'btn-outline-info','type':'checkbox','require':False},choices=ACTIVO),
                 'is_superuser':forms.Select(attrs={'style':'border: 1px solid black','class': 'selectpicker form-control text-center','data-style':'btn-outline-info','type':'checkbox','require':False},choices=SUPER),          
        }         
