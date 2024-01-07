from django.shortcuts import redirect, render
from .models import *

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

def carrito(request):
    carrito = Carrito.objects.all()
    return render(request, 'carrito.html', {'carrito': carrito})