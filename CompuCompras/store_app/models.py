from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100, default="Sin categoria")
    imagen = models.ImageField(upload_to="productos", null=True, blank=True)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.titulo
    
class Carrito(models.Model):
    productos = models.ManyToManyField(Producto, through='CarritoProducto')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    
    cantidad_productos = models.IntegerField(default=0, null=True)
    def __str__(self):
        return str(self.productos)

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

class Banner(models.Model):
    imagen = models.ImageField(upload_to="banners", null=True, blank=True)
    alt = models.CharField(max_length=100, null=True)
    
