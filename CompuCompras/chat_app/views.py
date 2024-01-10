from django.shortcuts import render
from .models import Mensaje
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def chat(request):
    todos_los_mesajes = Mensaje.objects.all()

    return render(request, 'chat.html', {'todos_los_mensajes': todos_los_mesajes})
