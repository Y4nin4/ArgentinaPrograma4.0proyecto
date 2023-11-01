import datetime
from django.db import models
from django.utils import timezone

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('Fecha publicada')

    def __str__(self):
        return self.texto_pregunta
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_opcion = models.CharField(max_length=200)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_opcion
