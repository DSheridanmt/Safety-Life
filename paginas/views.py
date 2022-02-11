

# Create your views here.

from django.views.generic import TemplateView

from .models import Publicacao

class HomeView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name  = 'login.html'

class PublicaçõesView(TemplateView):
    template_name = 'publicaçoess.html'



class PerfilView(TemplateView):
    template_name ='perfil.html'

class CadastroView(TemplateView):
    template_name ='cadastro.html'

class PublicacoesView(TemplateView):
    template_name = 'publicacoes.html'

   