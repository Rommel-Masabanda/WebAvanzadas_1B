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
    productos = models.ManyToManyField(Producto)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_productos = models.IntegerField()
    def __str__(self):
        return str(self.productos)
        
    
