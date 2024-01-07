from django.shortcuts import redirect, render
from .models import Producto

# Create your views here.


def ofertas(request):
    return render(request, 'ofertas.html')

def nuevos(request):
    return render(request, 'nuevos.html')

def get_productos(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def carrito(request):
    return render(request, 'carrito.html')