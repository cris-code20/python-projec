from distutils.command.upload import upload
from email.mime import image
from multiprocessing import set_forkserver_preload
from tokenize import blank_re
from django.db import models
from requests import delete

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    image = models.ImageField(upload_to='imagen/', verbose_name="imagen", null=True)
    descricion = models.TextField(verbose_name="descricion" ,null=True)
    # autor  = models.CharField(max_length=100)
    # genero = models.CharField(max_length=100)
    # anio   = models.IntegerField()
    # editor = models.CharField(max_length=100)
    # isbn   = models.CharField(max_length=100)
    # prezzo = models.FloatField()
    # disponibilidad = models.IntegerField()

    def __str__(self):
        fila =  "titulo: " + self.titulo + " - " + "descricion: " + self.descricion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()