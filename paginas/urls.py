from django.urls import path

from .views import AdminView, HomeView, LoginView, PublicacoesView

urlpatterns = [ 

    path('', HomeView.as_view(), name= 'home'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('admin/', AdminView.as_view(), name= 'admin'),
    path('publicaçoes/', PublicacoesView.as_view(), name= 'publicacoes'),

]