from datetime import datetime
from distutils.command.upload import upload
from turtle import window_height
from types import ClassMethodDescriptorType
from unittest.util import _MAX_LENGTH
import django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey
from django.forms import MultipleChoiceField
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    nomeTag = models.CharField(max_length= 40, verbose_name='Tag')

    def __str__(self):
        return self.nomeTag

class Publicacao(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título', editable=True)
    descricao = models.TextField(max_length=5000, verbose_name='Descrição', editable=True)
    hora = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='arquivos', blank=True, verbose_name='Imagem', editable=True)
    upload = models.FileField(upload_to='arquivos', blank=True, verbose_name='Arquivo', editable=True)
    link = models.URLField(max_length=200, blank=True, verbose_name='Link', editable=True)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo