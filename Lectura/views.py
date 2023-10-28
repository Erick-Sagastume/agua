from decimal import Decimal
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Lectura.models import Lectura
from Cliente.models import Cuenta
from Servicios.models import Servicio
from user.models import User
from django.contrib import messages
from datetime import datetime
import uuid
from Lectura.forms import LecturaForm
from django.db.models import Q # se usa para busqueda con coicidencia o exactas



@login_required
def lectura(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        #paginacion 
        comments = Lectura.objects.all().order_by("-id")
        paginator = Paginator(comments, 10) # Show 25 contacts per page.
 
        page_number = request.GET.get('page')
        comments_page = paginator.get_page(page_number)

        return render(request,'Lectura/Lectura.html',{'comments_page': comments_page,'lecturas':comments})
    

@login_required
def buscador2(request):
    b = False
    if request.method == "POST":
            cuenta = Cuenta.objects.filter(Q(dpi__nombre__icontains=request.POST['buscar'])|Q(id_cuenta__icontains=request.POST['buscar']))
            b = True
            return render(request,"Lectura/buscar2.html",{'cuenta':cuenta,'b':b})  
    
    return render(request,"Lectura/buscar2.html",{'b':b})

@login_required
def nuevalectura(request,cuenta):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        
        if Lectura.objects.filter(id_cuenta=cuenta).filter(id_cuenta=cuenta).exists():
            ultima = Lectura.objects.filter(id_cuenta=cuenta).order_by('mes').last()
        
            if ultima.actual == None:
                u = 0
            else:
                u = ultima.actual
                
                if request.method == "POST":
                    cuenta = Cuenta.objects.get(id_cuenta=request.POST['cuenta'])
                    miserv = cuenta.servicio
                    verlectura = Lectura.objects.filter(id_cuenta=request.POST['cuenta'],mes=request.POST['mes'],ciclo=datetime.today().strftime('%Y')).exists()
                    verservicio = Servicio.objects.get(id_servicio=miserv.id_servicio)
                    if verlectura:
                        messages.error(request,f'Error Al Ingresar Lectura del Mes de {request.POST["mes"]} ya ha sido asignada este mes a esta cuenta {request.POST["cuenta"]}')
                        return redirect('NuevaLectura',cuenta)
                    else:
                        try:
                            l = Lectura()
                            l.id_cuenta = Cuenta.objects.get(id_cuenta=cuenta)
                            l.anterior = float(request.POST['anterior'])
                            l.actual = float(request.POST['actual'])
                            l.consumo = l.actual-l.anterior
                            if l.consumo > verservicio.limite:
                                l.exceso = l.consumo-verservicio.limite
                                l.cargo_exceso = 3.00
                            else:
                                l.exceso = 0.00
                                l.cargo_exceso = 0.00

                            l.mes = request.POST['mes']
                            l.ciclo = datetime.today().strftime('%Y')
                            l.cargo_mes = verservicio.mensual
                            l.cargo_total = Decimal(l.cargo_mes)+Decimal(l.cargo_exceso)
                            l.usuario = User.objects.get(id=request.user.id)
                            l.fecha = datetime.today()
                            l.estado = 0
                            l.save()
                            messages.success(request,f'Lectura del Mes de {l.mes} Asginada a Cuenta {l.id_cuenta}!')
                            return redirect('NuevaLectura',cuenta)
                        except:
                            messages.error(request,f'Error Al Ingresar Lectura del Mes de {l.mes} a Cuenta {l.id_cuenta}')
                            return redirect('NuevaLectura',cuenta) 
            
            return render(request,'Lectura/nuevalectura.html',{'cuenta':cuenta,'u':u})    
        else:
            
            if Lectura.objects.filter(id_cuenta=cuenta).filter(id_cuenta=cuenta).exists():
                ultima = Lectura.objects.filter(id_cuenta=cuenta).order_by('mes').last()
                u = ultima.actual
            else:
                u = 0    
             
            if request.method == "POST":
                cuenta = Cuenta.objects.get(id_cuenta=request.POST['cuenta'])
                miserv = cuenta.servicio
                verlectura = Lectura.objects.filter(id_cuenta=request.POST['cuenta'],mes=request.POST['mes'],ciclo=datetime.today().strftime('%Y')).exists()
                verservicio = Servicio.objects.get(id_servicio=miserv.id_servicio)
                if verlectura:
                    messages.error(request,f'Error Al Ingresar Lectura del Mes de {request.POST["mes"]} ya ha sido asignada este mes a esta cuenta {request.POST["cuenta"]}')
                    return redirect('NuevaLectura',cuenta)
                else:
                    try:
                        l = Lectura()
                        l.id_cuenta = Cuenta.objects.get(id_cuenta=cuenta)
                        l.anterior = float(request.POST['anterior'])
                        l.actual = float(request.POST['actual'])
                        l.consumo = l.actual-l.anterior
                        if l.consumo > verservicio.limite:
                            l.exceso = l.consumo-verservicio.limite
                            l.cargo_exceso = 3.00
                        else:
                            l.exceso = 0.00
                            l.cargo_exceso = 0.00

                        l.mes = request.POST['mes']
                        l.ciclo = datetime.today().strftime('%Y')
                        l.cargo_mes = verservicio.mensual
                        l.cargo_total = Decimal(l.cargo_mes)+Decimal(l.cargo_exceso)
                        l.usuario = User.objects.get(id=request.user.id)
                        l.fecha = datetime.today()
                        l.estado = 0
                        l.save()
                        messages.success(request,f'Lectura del Mes de {l.mes} Asginada a Cuenta {l.id_cuenta}!')
                        return redirect('NuevaLectura',cuenta)
                    except:
                        messages.error(request,f'Error Al Ingresar Lectura del Mes de {l.mes} a Cuenta {l.id_cuenta}')
                        return redirect('NuevaLectura',cuenta)
            else:
                return render(request,'Lectura/nuevalectura.html',{'cuenta':cuenta,'u':u})

@login_required
def actualizalectura(request,id):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        cuenta = Lectura.objects.get(id=id)
        if request.method=="GET":
            form = LecturaForm(instance=cuenta)
        else:
            form = LecturaForm(request.POST,instance=cuenta)
            if form.is_valid():
                form.save()         
                messages.success(request, f'Lectura{id} Actualizado Exitosamente!.')
                return redirect('Lectura')
        

        return render(request,'Lectura/actualizalectura.html',{'form':form})







