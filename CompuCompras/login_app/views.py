from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'crearCuenta.html')

def sign_up(request):
    return render(request, 'sign-up.html')


