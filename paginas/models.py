from distutils.command.upload import upload
from types import ClassMethodDescriptorType
from unittest.util import _MAX_LENGTH
import django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    nomeTag = models.CharField(max_length= 20, verbose_name='Tag')

    def __str__(self):
        return self.nomeTag

class Publicacao(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título')
    descricao = models.TextField(max_length=200, verbose_name='Descrição')
    hora = models.DateField(auto_now_add=True)
    upload = models.FileField(upload_to='arquivos')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.titulo
