from types import ClassMethodDescriptorType
from django.db import models
from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Admin(models.Model):
    Nome = models.CharField(max_length=50)
    Senha = models.CharField(max_length=20)
    Email = models.EmailField(max_length=30)
    ID = models.CharField(max_length=14)

    def __str__(self):
        return self.Nome

class Publicacao(models.Model):
    Titulo = models.CharField(max_length=50, verbose_name='Título: ')
    Tag = models.CharField(max_length=30, verbose_name= 'Tag: ')
    Data_Atualizacao = models.DateField(auto_now=True, auto_now_add=True)
    ID_Publicacao = models.CharField(max_length=14)

    def __str__(self):
        return self.Titulo

class Exercicios(models.Model):
    Descricao = models.TextField(max_length=200, verbose_name='Descrição: ')
    ID_Exercicios = models.CharField(max_length=14)
    ID_Publicacao = models.ForeignKey(to=Publicacao, on_delete=models.PROTECT)

class Receitas(models.Model):
    Descricao = models.TextField(max_length=200, verbose_name='Descrição: ')
    Tag = models.CharField(max_length=30)
    ID_Receitas = models.CharField(max_length=14)
    ID_Publicacao = models.ForeignKey(to= Publicacao, on_delete=models.PROTECT)
