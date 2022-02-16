from django.urls import path

from .views import HomeView, LoginView, PublicacoesView

urlpatterns = [ 
    path('', HomeView.as_view(), name= 'home'),
    path('login/', LoginView.as_view(), name = 'login'),
   
    path('publicacoes/', PublicacoesView.as_view(), name= 'publicacoes'),

]