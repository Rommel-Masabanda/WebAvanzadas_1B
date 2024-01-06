from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# Create your views here.

class VLogearse(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            if usuario is not None:
                login(request, usuario)
                return redirect('index')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")
        

        return render(request, "login/login.html", {"form": form})


class VRegistrase(View):
    def get(self, request):
        form = UserCreationForm()
        form.fields['username'].help_text = ''
        form.fields['password1'].help_text = ''
        form.fields['password2'].help_text = ''
        return render(request, "sign-up.html", {"form": form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('index')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'sign-up.html', {"form": form})

def register(request):
    return render(request, 'crearCuenta.html')

def sign_up(request):
    return render(request, 'sign-up.html')


