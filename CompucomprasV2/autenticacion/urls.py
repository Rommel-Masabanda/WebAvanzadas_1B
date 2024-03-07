from django.urls import path
from .views import RegistroUsuario

urlpatterns = [
     path('register/', RegistroUsuario.as_view(), name='user_registration'),
]