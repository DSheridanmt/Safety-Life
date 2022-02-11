from django.urls import path
from .views import CadastroView, ExerciciosView, HomeView, LoginView, PerfilView, ReceitasView
urlpatterns = [ 
    path('', HomeView.as_view(), name= 'home'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('perfil/', PerfilView.as_view(), name= 'perfil'),
    path('cadastro/', CadastroView.as_view(), name= 'cadastro'),
    path('receitas/', ReceitasView.as_view(), name= 'receitas'),
    path('exercicios/', ExerciciosView.as_view(), name= 'exercicios'),
    
    
    

]