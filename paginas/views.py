# Create your views here.

from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Publicacao

class HomeView(TemplateView):
    template_name = 'index.html'

class PublicacoesView(TemplateView):
    template_name = 'publicacoes.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'




   