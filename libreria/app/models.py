from distutils.command.upload import upload
from email.mime import image
from tokenize import blank_re
from django.db import models

# Create your models here.

class Libro(models.Model):
    id     = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    image  = models.ImageField(upload_to='imagen/', verbose_name="imagen", null=True)
    descricion = models.TextField(verbose_name="descricion" ,null=True)
    # autor  = models.CharField(max_length=100)
    # genero = models.CharField(max_length=100)
    # anio   = models.IntegerField()
    # editor = models.CharField(max_length=100)
    # isbn   = models.CharField(max_length=100)
    # prezzo = models.FloatField()
    # disponibilidad = models.IntegerField()

    # def __str__(self):
    #     return self.titulo