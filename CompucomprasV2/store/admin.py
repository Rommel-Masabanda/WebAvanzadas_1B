from django.contrib import admin
from .models import  Producto, Carrito, CarritoProducto, Banner
# Register your models here.


admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(CarritoProducto)
admin.site.register(Banner)
