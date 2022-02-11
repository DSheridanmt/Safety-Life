

# Create your views here.

from django.views.generic import TemplateView

from .models import Publicacao

class HomeView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name  = 'login.html'

class PublicaçõesView(TemplateView):
    template_name = 'publicaçoess.html'


class AdminView(TemplateView):
    template_name = 'admin.html'
   