from django.urls import path, include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register(r'producto', views.ProductoViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('agregar-producto-al-carrito/', views.AgregarProductoAlCarrito.as_view(), name='agregar_producto_al_carrito'),
    path('obtenerCarrito/', views.ObtenerCarrito.as_view(), name='obtener_carrito'),
    path('eliminarProductosCarrito/', views.EliminarProductoDelCarrito.as_view(), name='eliminar_carrito'),
    path('realizarCompra/', views.RealizarCompra.as_view(), name='realizar_compra'),
]
