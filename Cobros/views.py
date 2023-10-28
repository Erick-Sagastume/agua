from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user.models import User
from datetime import datetime
from django.contrib import messages
from django.db.models import Sum
from Lectura.models import Lectura # tabla de las lecturas
from Cliente.models import Cliente,Cuenta
from django.core.paginator import Paginator
#from Cobros.models import Cobro
from django.db.models import Q # se usa para busqueda con coicidencia o exactas


@login_required
def lista(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        lectura = Lectura.objects.filter(estado=1)
        return render(request,'Cobros/lista.html',{'lectura':lectura})
    
@login_required
def cobros(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
       if request.method == 'POST':
           
           ver = Cuenta.objects.filter(id_cuenta=request.POST['cuenta']).exists()# busca la cuenta y si tiene pediente pago
           if ver:
                datos = Lectura.objects.filter(id_cuenta=request.POST['cuenta'],estado=0).exists()
                if datos:
                    messages.success(request,'Cuenta Existe')
                    messages.success(request,'Cuenta Tiene Cobro Pendiente')
                    return redirect('NuevoCobro',request.POST['cuenta'])
                else:
                    messages.success(request,'Cuenta Existe')
                    messages.success(request,'Cuenta Al Dia')
                    return redirect('Cobros')

           else:
               messages.error(request,'Cuenta NO Existe')
               return redirect('Cobros')
                   
       return render(request,'Cobros/despacho.html')
   

@login_required
def buscador(request):
    b = False
    if request.method == "POST":
            cuenta = Cuenta.objects.filter(Q(dpi__nombre__icontains=request.POST['buscar'])|Q(id_cuenta__icontains=request.POST['buscar']))
            b = True
            datos_lectura = Lectura.objects.filter(id_cuenta=id,estado=0) 
            return render(request,"Cobros/buscar.html",{'cuenta':cuenta,'b':b,'lecturas':datos_lectura})  
    
    return render(request,"Cobros/buscar.html",{'b':b})


@login_required
def nuevo(request,id):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
       datos_cliente = Cuenta.objects.get(id_cuenta=id) # jalamos los datos del propietario y del servicio
       datos_lectura = Lectura.objects.filter(id_cuenta=id,estado=0) 
       adeuda = Lectura.objects.filter(id_cuenta=id,estado=0).aggregate(total=Sum('cargo_total'))

       if 'pagar' in request.POST:
           Lectura.objects.filter(id=request.POST['correlativo'],estado=0).update(estado=1)
           messages.success(request,'Mes Pagado!')
           return redirect('NuevoCobro',id)
       elif 'fin' in request.POST:
           messages.success(request,f'Cobro Finalizado Para Cuenta {id}!')
           return redirect('Cobros')

       return render(request,'Cobros/detalles.html',{'cliente':datos_cliente,'lecturas':datos_lectura,'adeuda':adeuda['total']})


   