from django.db import models

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.titulo
    
class Carrito(models.Model):
    productos = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_productos = models.IntegerField()
    def __str__(self):
        return str(self.productos)
        
    
