from django.urls import path
<<<<<<< HEAD
from .views import CadastroView, ExerciciosView, HomeView, LoginView, PerfilView, PublicacoesView, ReceitasView
=======
from .views import CadastroView, HomeView, LoginView, PerfilView, PublicaçõesView
>>>>>>> afa862c3c6270bfc9023b2397ee9241d73474407
urlpatterns = [ 
    path('', HomeView.as_view(), name= 'home'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('perfil/', PerfilView.as_view(), name= 'perfil'),
    path('cadastro/', CadastroView.as_view(), name= 'cadastro'),
<<<<<<< HEAD
    path('receitas/', ReceitasView.as_view(), name= 'receitas'),
    path('exercicios/', ExerciciosView.as_view(), name= 'exercicios'),
    path('publicacoes/', PublicacoesView.as_view(), name= 'publicacoes')
=======
    path('publicaçoes/', PublicaçõesView.as_view(), name= 'publicaçoes'),
   
    
>>>>>>> afa862c3c6270bfc9023b2397ee9241d73474407
    
    

]