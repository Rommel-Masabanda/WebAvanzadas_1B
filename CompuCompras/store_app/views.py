from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ofertas(request):
    return render(request, 'ofertas.html')

def nuevos(request):
    return render(request, 'nuevos.html')

def carrito(request):
    return render(request, 'carrito.html')