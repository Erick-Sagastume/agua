from uuid import UUID
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Cliente.models import Cliente,Cuenta
from Servicios.models import Servicio
from Lectura.models import Lectura
from user.models import User
from django.contrib import messages
from datetime import datetime
import uuid
from Cliente.forms import ClienteForm,CuentaForm
from .reportes import ReportePagos, ReportePagos2

@login_required
def cliente(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        #paginacion 
        comments = Cliente.objects.filter(estado=1)
        paginator = Paginator(comments, 10) # Show 25 contacts per page.
 
        page_number = request.GET.get('page')
        comments_page = paginator.get_page(page_number)

        return render(request,'Cliente/cliente.html',{'comments_page': comments_page,'cliente':comments})
    

def listacliente(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        usuarios = Cliente.objects.filter(is_active=1)
        return render(request,"Cliente/cliente.html",{'usuarios':usuarios})



def listacliente2(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        clientes = Cliente.objects.filter(estado=0)
        return render(request,"Cliente/cliente2.html",{'cliente':clientes})
    
def cuenta2(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        cuenta2 = Cuenta.objects.filter(estado=0)
        return render(request,"Cliente/cuenta2.html",{'cuenta':cuenta2})
    
@login_required
def nuevo(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        
        if request.method == "POST":
            try:
                c = Cliente()
                c.dpi = request.POST['dpi']
                c.nombre = request.POST['nombre']
                c.apellido = request.POST['apellido']
                c.direccion = request.POST['direccion']
                c.telefono = request.POST['telefono']
                c.correo = request.POST['correo']
                c.usuario = User.objects.get(id=request.user.id)
                c.fecha = datetime.today()
                c.estado = 1
                c.save()
                messages.success(request,'Cliente Ingresado!')
                return redirect('Cliente')
            except:
                messages.error(request,'Error Al Ingresar Cliente')
                return redirect('NuevoCliente')
        else:
            return render(request,'Cliente/nuevo.html')


@login_required
def detalleservicios(request,id):
    c=Cuenta.objects.filter(dpi=id)
    
    return render(request,'Cliente/detalleserviciocliente.html',{'c':c}) 

@login_required
def detallepagoscliente(request,id):
  
    c = Lectura.objects.filter(id_cuenta=id,estado=1)
    
    return render(request,'Cliente/detallepagoscliente.html',{'c':c})  


def pdf(request,id):
   if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
   else: 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="comprobante-pagos-#-{id}.pdf"'
    r = ReportePagos(id)
    response.write(r.run())
    return response

def pdf2(request,id,mes):
   if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
   else: 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="comprobante-pagos-#-{id}.pdf"'
    r = ReportePagos2(id,mes)
    response.write(r.run())
    return response



@login_required
def cuenta(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        #paginacion 
        comments = Cuenta.objects.filter(estado=1)
        paginator = Paginator(comments, 10) # Show 25 contacts per page.
 
        page_number = request.GET.get('page')
        comments_page = paginator.get_page(page_number)

        return render(request,'Cliente/cuenta.html',{'comments_page': comments_page,'cuenta':comments})

    
@login_required
def actualizacuenta(request,id):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        cuenta = Cuenta.objects.get(id_cuenta=id)
        if request.method=="GET":
            form = CuentaForm(instance=cuenta)
        else:
            form = CuentaForm(request.POST,instance=cuenta)
            if form.is_valid():
                form.save()         
                messages.success(request, f'Cuenta{id} Actualizado Exitosamente!.')
                return redirect('Cuenta')
        

        return render(request,'Cliente/actualizacuenta.html',{'form':form})
    
    
@login_required
def bajacuenta(request,cuenta):
    try:
        dato = Cuenta.objects.get(id_cuenta=cuenta)
        Cuenta.objects.filter(id_cuenta=cuenta).update(estado=0)
        messages.success(request,f'{dato.id_cuenta} ha sido dada de baja!')
        return redirect('Cuenta')
    except:
        messages.error(request,f'{dato.id_cuenta} NO ha sido dada de baja ERROR!')
        return redirect('Cuenta')
    
@login_required
def altacuenta(request,cuenta):
    try:
        dato = Cuenta.objects.get(id_cuenta=cuenta)
        Cuenta.objects.filter(id_cuenta=cuenta).update(estado=1)
        messages.success(request,f'{dato.id_cuenta} ha sido dada de alta!')
        return redirect('Cuenta')
    except:
        messages.error(request,f'{dato.id_cuenta} NO ha sido dada de baja ERROR!')
        return redirect('Cuenta')


@login_required
def bajacliente(request,dpi):
    try:
        elcliente = Cliente.objects.get(dpi=dpi)
        cuentas = Cuenta.objects.filter(dpi=dpi)   

        Cliente.objects.filter(dpi=dpi).update(estado = 0)
        elcliente.update(estado = 0)

        messages.success(request,f'{elcliente.nombre} ha sido de baja junto con sus cuentas!')
        return redirect('Cliente')

    except:
        messages.error(request,f'{elcliente.nombre} ')
        return redirect('Cliente')

@login_required
def altacliente(request,dpi):
    try:
        elcliente = Cliente.objects.get(dpi=dpi)
        cuentas = Cuenta.objects.filter(dpi=dpi)   

        Cliente.objects.filter(dpi=dpi).update(estado = 1)
        elcliente.update(estado = 1)

        messages.success(request,f'{elcliente.nombre} ha sido de dado de Alta junto con sus cuentas!')
        return redirect('Cliente')

    except:
        messages.error(request,f'{elcliente.nombre} ')
        return redirect('Cliente')

@login_required
def nuevacuenta(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        servicio= Servicio.objects.all()
        if request.method == "POST":
            try:
                c = Cuenta()
                c.id_cuenta = request.POST['cuenta']
                c.dpi = Cliente.objects.get(dpi=request.POST['dpi'])
                c.servicio = Servicio.objects.get(id_servicio=request.POST['tipo'])
                c.direccion = request.POST['direccion']
                c.usuario = User.objects.get(id=request.user.id)
                c.fecha = datetime.today()
                c.save()
                micuenta = Cuenta.objects.filter(dpi=c.dpi).last()
                messages.success(request,f'Cuenta {micuenta.id_cuenta} Dada de Alta!')
                return redirect('Cuenta')
            except:
                messages.error(request,'Error Al Ingresar Nueva Cuenta')
                return redirect('NuevaCuenta')
        else:
            return render(request,'Cliente/nuevacuenta.html', {'servicio':servicio})
        

@login_required
def eliminar(request,id):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        try:
            Cuenta.objects.filter(dpi=id).delete()
            Cliente.objects.get(dpi=id).delete()
            messages.success(request,'Usario del Servicio Eliminados!')
            return redirect('Cliente')
        except:
            messages.success(request,'No Se Puedo Eliminar a Asociados y Buses de Asociado!')
            return redirect('Cliente')   
        
        
@login_required
def actualizarcliente(request, id):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        cliente = Cliente.objects.get(dpi=id)
        if request.method=="GET":
            form = ClienteForm(instance=cliente)
        else:
            form = ClienteForm(request.POST,instance=cliente)
            if form.is_valid():
                form.save()         
                messages.success(request, f'Cliente{id} Actualizado Exitosamente!.')
                return redirect('Cliente')
        

        return render(request,'Cliente/clienteactualiza.html',{'form':form})