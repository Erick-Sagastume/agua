from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Cliente.models import Cliente 
from Servicios.models import Servicio
from user.models import User
from django.contrib import messages
from datetime import datetime
from Servicios.forms import ServicioForm


@login_required
def servicios(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        #paginacion 
        comments = Servicio.objects.filter(estado=1)
        paginator = Paginator(comments, 10) # Show 25 contacts per page.
 
        page_number = request.GET.get('page')
        comments_page = paginator.get_page(page_number)

        return render(request,'Servicios/lista.html',{'comments_page': comments_page,'servicio':comments}) 

@login_required
def lista(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        servicios=Servicio.objects.filter(estado=1)
        return render(request,'Servicios/lista.html',{'servicios':servicios})
    
def lista2(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        servicios = Servicio.objects.filter(estado=0)
        return render(request,"Servicios/lista2.html",{'servicios':servicios})
    

@login_required
def nuevo(request):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        servicios=Servicio.objects.all()
        if request.method == 'POST':
            s = Servicio()
            s.nombre = request.POST['nombre']
            s.limite = request.POST['limite']
            s.mensual = request.POST['mensual']
            s.fecha = datetime.today()
            s.usuario = User.objects.get(id=request.user.id)
            s.save()
            messages.success(request,f'Servicio {s.nombre} ingresado!')
            return redirect('ListaServicio')
        

        return render(request,'Servicios/nuevo.html',{'servicio':servicios})


@login_required
def eliminarservicio(request, id):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        try:
            Servicio.objects.get( id_servicio=id).delete()
            messages.success(request, f'Servicio{id} Eliminado Exitosamente!.')
            return redirect('Servicio')
        except:
            messages.error(request, f'Servicios {id} Eliminacion Fallida!.')
            return redirect('ListaServicio')
                
          
          

@login_required
def actualizar(request, id):
    if not request.user.is_authenticated and not request.user.is_active:
        return redirect('/')
    else:
        servicios = Servicio.objects.get(id_servicio=id)
        if request.method=="GET":
            form = ServicioForm(instance=servicios)
        else:
            form = ServicioForm(request.POST,instance=servicios)
            if form.is_valid():
                form.save()         
                messages.success(request, f'Servicios{id} Actualizado Exitosamente!.')
                return redirect('ListaServicio')
        

        return render(request,'Servicios/updateservicio.html',{'form':form})
    

@login_required
def bajaservicio(request,id):
    try:
        dato = Servicio.objects.get(id_servicio=id)
        Servicio.objects.filter(id_servicio=id).update(estado=0)
        messages.success(request,f'{dato.id_servicio} ha sido dado de baja!')
        return redirect('ListaServicio')
    except:
        messages.error(request,f'{dato.id_servicio} NO ha sido dada de baja ERROR!')
        return redirect('ListaServicio')
    
@login_required
def altaservicio(request,id):
    try:
        dato = Servicio.objects.get(id_servicio=id)
        Servicio.objects.filter(id_servicio=id).update(estado=1)
        messages.success(request,f'{dato.id_servicio} ha sido dado de alta!')
        return redirect('ListaServicio')
    except:
        messages.error(request,f'{dato.id_servicio} NO ha sido dada de baja ERROR!')
        return redirect('ListaServicio')