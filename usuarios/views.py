from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout

import django
# Create your views here.
from catalogo.models import Categoria, Producto
from usuarios.models import Propietario
from django.http import JsonResponse

def valencia_refa(request):
    if request.method=="POST":
        name = request.POST.get('username')
        #passwd = request.POST.get('password')  
        passwd = 'encia1234'     
        user = authenticate(request, username=name, password=passwd)
        if user is not None:
            login(request, user) 
            #id_user_activo = request.user.id
            categorias=Categoria.objects.filter(esta_activa=True, propietario_id=request.user.id)
            context={'categorias':categorias}
            return render(request, 'catalogo/collections.html', context)

    return render(request, 'usuarios/valencia_refa.html')

def sisma_pv(request):
    if request.method=="POST":
        name = request.POST.get('username')
        #passwd = request.POST.get('password')        
        passwd = 'For4Amsis'
        user = authenticate(request, username=name, password=passwd)
        if user is not None:
            login(request, user) 
            usuario = Propietario.objects.filter(id=request.user.id).first()
            #print(usuario) 
            el_user_esta_activo = usuario.esta_activo            
            categorias=Categoria.objects.filter(esta_activa=True, propietario_id=request.user.id)
            context={'categorias':categorias, 'usuario':usuario }
            if el_user_esta_activo:
                return render(request, 'catalogo/collections.html', context)
            else:
                return render(request,'usuarios/404.html')

    return render(request, 'usuarios/sisma_pv.html')


def despedida(request):
    auth_logout(request)
    return render(request, 'usuarios/despedida.html')

def productlistAjax(request):
    products=Producto.objects.filter( propietario_id=request.user.id).values_list('producto', flat=True)
    productsList= list(products)

    return JsonResponse(productsList, safe=False)

def searchproduct(request): 
    if request.method =="POST":
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect( request.META.get('HTTP_REFERER'))
        else:
            elproducto = Producto.objects.filter(producto__contains=searchedterm).first()
            if elproducto:
                return redirect('producto_a_editar/'+elproducto.slug)
            else:
                # buscar por codigo de barras
                elproducto = Producto.objects.filter(cod_barras__contains=searchedterm).first()
                if elproducto:
                    return redirect('producto_a_editar/'+elproducto.slug)
                else:

                    messages.info(request, "Ningun producto para el criterio!")
                    return redirect( request.META.get('HTTP_REFERER'))

    return redirect( request.META.get('HTTP_REFERER'))

def handling_404(request):
    return django.views.defaults.page_not_found(request, None)
