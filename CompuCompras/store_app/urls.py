from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevos', views.nuevos, name='nuevos'),
    path('ofertas', views.ofertas, name='ofertas')    
]