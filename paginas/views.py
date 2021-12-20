

# Create your views here.

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name  = 'login.html'

class ReceitasView(TemplateView):
    template_name = 'receitas.html'

class ExerciciosView(TemplateView):
    template_name ='exercicios.html'

class PerfilView(TemplateView):
    template_name ='perfil.html'

class SobreView(TemplateView):
    template_name ='sobre.html'

class CadastroView(TemplateView):
    template_name ='cadastro.html'

class LogoutView(TemplateView):
    template_name ='logout.html'