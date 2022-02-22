from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image=models.CharField(max_length=10000)
    class Meta:
        db_table='pages_noticia'