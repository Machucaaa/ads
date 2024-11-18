from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from catalogo.models import Producto
from catalogo.models import Cart, Orden
from usuarios.models import Cliente, Propietario
from usuarios.forms import ClienteForm

def addtocart(request): 
    if request.method == 'POST':
        #if request.user.is_authenticated:
        device = request.COOKIES['device']
        check_cliente = Cliente.objects.filter(device=device).first()
        if check_cliente is None:
            se_creo_cliente = True
            cliente, created = Cliente.objects.get_or_create(device=device)
            check_cliente = cliente
        else:
            se_creo_cliente = False
        prod_id = int(request.POST.get('product_id'))
        prod_qty = int(request.POST.get('product_qty'))
        product_check = Producto.objects.get(Id_producto = prod_id)
        # como establecer el cliente
        clienteact = check_cliente
        id_cliente = clienteact.id_cliente
        # falta verificar stock (min 19:48 part 11)
        #print(clienteact) 
        #print(prod_id)
        cliente_y_prod = Cart.objects.filter(cliente_id=id_cliente, id_producto_id=prod_id).first()
        if cliente_y_prod is not None: 
            return JsonResponse({'status': 'Producto ya en carrito'})

        else:
            cart, created =Cart.objects.get_or_create(cliente_id=id_cliente, id_producto_id=prod_id, product_qty=prod_qty)
            return JsonResponse({'status': 'añadido al carrito'})

def addToOrden(request):

    device = request.COOKIES['device']
    clienteQueOrdena = Cliente.objects.filter(device=device).first()
    idClienteQueOrdena = clienteQueOrdena.id_cliente
    nvaOrden = Orden.objects.create(cliente_id = idClienteQueOrdena)
    #nvaOrden.cliente_id = idClienteQueOrdena
    #nvaOrden.save() 
    idNvaOrden = nvaOrden.id   
    Cart.objects.filter(cliente_id=idClienteQueOrdena).update(orden_id=idNvaOrden)                

    print('Creacion de orden!')
    return redirect('despedida')
    #return JsonResponse({'status': 'Orden creada!'})


def viewcart(request):
    device = request.COOKIES['device']
    check_cliente = Cliente.objects.filter(device=device).last()
    if check_cliente.nombre is None :
        #print("a regcliente")
        return redirect('logincliente')
    id_clienteact = check_cliente.id_cliente
    cart = Cart.objects.filter(cliente_id=id_clienteact)
    #print(cart)
    cliente = Cliente.objects.get(device=device)
    context = {'cart': cart, 'cliente': cliente}
    return render(request,"usuarios/cart.html", context )

def updatecart(request):
    if request.method == 'POST':
        #if request.user.is_authenticated:
        device = request.COOKIES['device']
        check_cliente = Cliente.objects.get(device=device)

        prod_id = int(request.POST.get('product_id'))
        prod_qty = int(request.POST.get('product_qty'))
        # como establecer el cliente
        clienteact = check_cliente.id_cliente
        # falta verificar stock (min 19:48 part 11)
        #print(clienteact) 
        #print(prod_id)
        cart = Cart.objects.get(cliente_id=clienteact, id_producto_id=prod_id)
        if cart is not None: 
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': 'cantidad actualizada'})
    return redirect('collections')  

def deletecartitem(request):
    if request.method == 'POST':
        #if request.user.is_authenticated:
        device = request.COOKIES['device']
        check_cliente = Cliente.objects.get(device=device)

        prod_id = int(request.POST.get('product_id'))
        # como establecer el cliente
        clienteact = check_cliente.id_cliente
        cartitem = Cart.objects.get(cliente_id=clienteact, id_producto_id=prod_id)
        if cartitem is not None: 
            cartitem.delete()
            return JsonResponse({'status': 'Borrado'})
        else:
            return JsonResponse({'status': 'No es el producto'})
    return redirect('collections')  

def regcliente(request):
    form = ClienteForm
    if request.method =='POST':
        form = ClienteForm(request.POST)
               
        if form.is_valid():
            device = request.COOKIES['device']
            nombre = request.POST.get('nombre')
            whatsapp = request.POST.get('whatsapp')
            password = request.POST.get('password')
            whatsappa = request.POST.get('whatsappa')
            cliente = Cliente.objects.get(device=device)
            cliente.nombre = nombre 
            cliente.whatsapp = whatsapp
            cliente.proveedor = request.user
            cliente.password = password
            cliente.whatsappa = whatsappa 
            cliente.save() 
            messages.error(request, 'Registrado!') 
            return redirect('collections')

    context = {'form' : form }
    return render(request,'usuarios/auth/regcliente.html', context )
