from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_productos, name='index'),
    path('nuevos', views.nuevos, name='nuevos'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('carrito/', views.get_carrito, name='carrito'),   
    path('agregar_al_carrito/', views.agregar, name='agregar'),
    path('eliminar_del_carrito/', views.eliminar, name='eliminar'),
]