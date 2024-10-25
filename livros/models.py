from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=200, null=True, blank=True)
    autor = models.CharField(max_length=100, null=True, blank=True)
    data_publicacao = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)

    def __str__(self):
        return self.titulo