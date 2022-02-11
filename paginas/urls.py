from django.urls import path
from .views import CadastroView, HomeView, LoginView, PerfilView, PublicaçõesView
urlpatterns = [ 
    path('', HomeView.as_view(), name= 'home'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('perfil/', PerfilView.as_view(), name= 'perfil'),
    path('cadastro/', CadastroView.as_view(), name= 'cadastro'),
    path('publicaçoes/', PublicaçõesView.as_view(), name= 'publicaçoes'),
   
    
    
    

]