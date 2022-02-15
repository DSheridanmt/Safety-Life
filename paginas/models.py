from types import ClassMethodDescriptorType
from django.db import models
from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Admin(models.Model):
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nomeTag = models.CharField(max_length= 20, verbose_name='Tag')

    def __str__(self):
        return self.nomeTag

class Publicacao(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título')
    descricao = models.TextField(max_length=200, verbose_name='Descrição')
    data_Atualizacao = models.DateField(auto_now=False, auto_now_add=True)
    hora = models.TimeField(auto_now=False, auto_now_add=True)
    id_Publicação= models.CharField(max_length=14, verbose_name= 'ID da publicação')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo
