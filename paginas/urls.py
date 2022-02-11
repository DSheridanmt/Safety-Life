from django.urls import path

from .views import CadastroView, HomeView, LoginView, PerfilView, PublicacoesView

urlpatterns = [ 
    path('', HomeView.as_view(), name= 'home'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('perfil/', PerfilView.as_view(), name= 'perfil'),
    path('cadastro/', CadastroView.as_view(), name= 'cadastro'),
    path('publicacoes/', PublicacoesView.as_view(), name= 'publicacoes'),
    
    

]