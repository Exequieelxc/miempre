from django.db import models

class Emprendimiento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='emprendimientos/', null=True, blank=True)
    estado = models.CharField(max_length=20, choices=[('disponible', 'Disponible'), ('no_disponible', 'No Disponible')])
    def __str__(self):
        return self.nombre