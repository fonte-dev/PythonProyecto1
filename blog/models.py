from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = "B", "Borrador"
        PUBLICADO = "P", "Publicado"

    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.BORRADOR
    )

    def __str__(self) -> str:
        return self.titulo
