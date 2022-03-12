# Create your views here.

from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Publicacao, Tag

class HomeView(TemplateView):
    template_name = 'index.html'

class PublicacoesView(ListView):
    template_name = 'publicacoes.html'
    model = Publicacao
    def get_queryset(self, *args, **kwargs):
        qs = super(PublicacoesView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

class SobreView(TemplateView):
    template_name = 'sobre.html'