from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_productos, name='index'),
    path('nuevos', views.nuevos, name='nuevos'),
    path('ofertas', views.ofertas, name='ofertas'),
    path('carrito/', views.carrito, name='carrito'),   
]