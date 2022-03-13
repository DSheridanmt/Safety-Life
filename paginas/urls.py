from django.urls import path

from .views import HomeView, PublicacoesView, SobreView

urlpatterns = [ 
    path('', HomeView.as_view(), name= 'home'),
   
    path('publicacoes/', PublicacoesView.as_view(), name= 'publicacoes'),

    path('sobre/', SobreView.as_view(), name='sobre'),


]