from django.db import models

# Create your models here.

class Actividades(models.Model):
    normativa = models.TextField(default='no indicada')
    actividad = models.TextField(default='no suministrado')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['-normativa', '-actualizado']

    def __str__(self):
        return self.normativa

class Normativa(models.Model):
    provincia = models.CharField(max_length=255, default='no suministrado')
    norma = models.CharField(max_length=255, default='no suministrado')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Norma'
        verbose_name_plural = 'Normas'
        ordering = ['-provincia', '-norma', '-actualizado']