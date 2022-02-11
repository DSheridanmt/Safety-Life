from django.urls import path
from .views import HomeView, LoginView, PublicaçõesView, AdminView
urlpatterns = [ 
    path('index/', HomeView.as_view(), name= 'index'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('admin/', AdminView.as_view(), name= 'admin'),
    path('publicaçoes/', PublicaçõesView.as_view(), name= 'publicaçoes'),
   
    
    
    

]