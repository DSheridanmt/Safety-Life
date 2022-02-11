from django.urls import path

from .views import AdminView, HomeView, LoginView, PublicacoesView
[
    path('', HomeView.as_view(), name= 'home'),
    path('admin/', AdminView.as_view(), name = 'admin'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('publicacoes/', PublicacoesView.as_view(), name= 'publicacoes'),


]