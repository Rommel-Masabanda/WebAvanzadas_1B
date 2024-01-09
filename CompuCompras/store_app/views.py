from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.contrib import messages
# Create your views here.


def ofertas(request):
    productos = Producto.objects.all()
    return render(request, 'ofertas.html',{'productos': productos})

def nuevos(request):
    productos = Producto.objects.all()
    return render(request, 'nuevos.html', {'productos': productos})

def get_productos(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})


def agregar(request):
    id_producto = request.POST['producto_id']
    producto = Producto.objects.get(id=id_producto)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    
    # Buscar si el producto ya está en el carrito
    item_carrito, creado_item = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
    
    # Incrementar la cantidad del producto en el carrito
    if not creado_item:
        item_carrito.cantidad += 1
        item_carrito.save()
    else:
        # Si se crea un nuevo item_carrito, establece la cantidad en 1
        item_carrito.cantidad = 1
        item_carrito.save()
    carrito.total += producto.precio
    carrito.cantidad_productos += 1
    carrito.save()
    messages.success(request, 'Añadido al carrito')
    return redirect(request.META.get('HTTP_REFERER', '/'))
    
def get_carrito(request):
    carritos = Carrito.objects.filter(usuario=request.user).prefetch_related('productos')
    banners = Banner.objects.all()
    return render(request, 'carrito.html', {'carritos': carritos, 'banners': banners})



def eliminar(request):
    if request.method == 'POST':
        item_carrito_id = request.POST['item_carrito_id']
        item_carrito = get_object_or_404(CarritoProducto, id=item_carrito_id)
        
        cantidad_producto = item_carrito.cantidad
        precio_producto = item_carrito.producto.precio

        carrito = item_carrito.carrito
        
        carrito.total -= precio_producto
        
        if cantidad_producto > 1:
            item_carrito.cantidad -= 1
            item_carrito.save()
        else:
            item_carrito.delete()
            carrito.cantidad_productos -= 1  
        
        carrito.save()
        
        messages.success(request, 'Producto eliminado del carrito')
        return redirect(request.META.get('HTTP_REFERER', '/'))
