from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib import messages

from usuarios.models import Propietario, Cliente
from catalogo.models import Cart
from usuarios.forms import CustomUserForm, ClienteForm, LoginClienteForm

def register(request): 
    form = CustomUserForm
    if request.method =='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request, 'Registrado, revise su email!') 
            return redirect('/para_editar_catalogo')
    context = {'form' : form }
    return render(request,'usuarios/auth/register.html', context )

def loginpage(request):
    auth_logout(request)
    if request.method=="POST":
        name = request.POST.get('username')
        passwd = request.POST.get('password')       
        user = authenticate(request, username=name, password=passwd)
        if user is not None:
            estaActivo = user.esta_activo
            if estaActivo:
                login(request, user) 
                messages.error(request, 'Ingreso Correcto!')
                return redirect('altascategoria')
            else:
                messages.error(request, 'Tu cuenta no esta activa!')
                return redirect('/para_editar_catalogo')
        else:
            messages.error(request, 'Nombre de usuario o password no validos!')
            return redirect('/para_editar_catalogo')
    return render( request, 'usuarios/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('/para_editar_catalogo')
    return redirect('/para_editar_catalogo')

def logincliente(request):
    form = LoginClienteForm
    if request.method =='POST':
        form = LoginClienteForm(request.POST)
               
        if form.is_valid():  
            device = request.COOKIES['device']
            whatsapp = request.POST.get('whatsapp')
            password = request.POST.get('password')

            #propietario = .objects.get(device=device)
            cliente = Cliente.objects.get(whatsapp= whatsapp, password=password)
            if cliente is None:
                messages.error(request, 'whatsapp o password incorrecto!') 
                return redirect('collections')
            else:
                cliente.device = device
                cliente.save()
                id_nuevo = cliente.id_cliente
                Cart.objects.filter(cliente_id=id_nuevo, orden_id = None).delete()                
                clientevacio=Cliente.objects.filter(device=device).last()
                id_viejo = clientevacio.id_cliente
                #clientevacio.delete()

                Cart.objects.filter(cliente_id=id_viejo).update(cliente_id=id_nuevo)                
                clientevacio.delete()
                messages.error(request, 'Ingreso correctamente!') 
                #return redirect('collections')
                return redirect('cart')
        else:
            messages.error(request, 'Hay un error!') 

    context = {'form' : form }
    return render(request,'usuarios/auth/logincliente.html', context )

