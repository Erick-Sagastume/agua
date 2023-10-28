from django.shortcuts import render,redirect
from user.models import User
from user.forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from uuid import UUID
from django.shortcuts import render,redirect
from django.core.paginator import Paginator

    
def nuevousuario(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        form = RegistroForm()
        if request.method == "POST":
            form = RegistroForm(request.POST)
            if form.is_valid():
                try:
                    u = User()
                    u.username = form.cleaned_data["username"]
                    u.password = make_password(form.cleaned_data["password"])
                    u.first_name = form.cleaned_data["first_name"]
                    u.last_name = form.cleaned_data["last_name"]
                    u.email = form.cleaned_data["email"]
                    u.rol = form.cleaned_data["rol"]
                    u.is_staff = form.cleaned_data["is_staff"]
                    u.is_active = form.cleaned_data["is_active"]
                    u.is_superuser = form.cleaned_data["is_superuser"]
                    u.save()
                    messages.success(request,'Registro de Usuario Exitoso')
                    return redirect('NuevoUser')
                except:
                    messages.error(request,'Registro de Usuario Fallido')
                    return redirect('NuevoUser')

            else:
                messages.error(request,"Formulario Corrupto")
                return redirect('NuevoUser')


        return render(request,"user/nuevousuario.html",{'form':form})


def listausuario(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        usuarios = User.objects.filter(is_active=1)
        return render(request,"user/todousuario.html",{'usuarios':usuarios})



def listausuario2(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        usuarios = User.objects.filter(is_active=0)
        return render(request,"user/todousuario2.html",{'usuarios':usuarios})

def updateusuario(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
         usuarios = User.objects.get(username=id)
         if request.method == 'GET':
            form = RegistroForm(instance=usuarios)
         else:
            form = RegistroForm(request.POST,request.FILES,instance = usuarios)
     
            if form.is_valid():
                try:
                    usuarios.password = make_password(form.cleaned_data['password'])
                    form.save()
                    messages.success(request, 'Usuario Modificado Exitosamente!.')
                    return redirect('/')
                except:
                    messages.error(request, 'Modificacion de Usuario Fallido!.')
                    return redirect('ListaUser')

    
    return render(request,"user/updateusuario.html",{'form':form,'d':id})






def deleteusuario(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        usuarios = User.objects.get(username=id)
        print(usuarios.username)
        if usuarios.username == request.user:
            messages.error(request, 'No Puedes Eliminar Tu Propio Usuario!.')
            return redirect('ListaUser')          
         
        else:
            if request.method == 'GET':
                try:
                    usuarios.delete() 
                    messages.success(request, 'Usuario Eliminado Exitosamente!.')
                    return redirect('ListaUser')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
                except:
                    messages.error(request, 'Eliminacion de Usuario Fallido!.')
                    return redirect('ListaUser') # path('error/',views.error,name="Error"),
            else:
              pass           
  




