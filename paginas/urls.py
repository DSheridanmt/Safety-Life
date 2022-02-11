from django.urls import path

from .views import HomeView, LoginView, PublicaçoesView, AdminView

urlpatterns = [ 
    path('', HomeView.as_view(), name= 'home'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('admin/', AdminView.as_view(), name= 'admin'),
    path('publicaçoes/', PublicaçoesView.as_view(), name= 'publicaçoes'),

]