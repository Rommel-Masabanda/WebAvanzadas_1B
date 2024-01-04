from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    mensaje = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username}: {self.mensaje}'
