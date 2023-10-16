from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('cadastroCriancas', views.cadastrarCriancas, name='CadastroCriancas'),
    path('ListarCriancas', views.ListarCriancas, name='ListarCriancas'),
    path('inicialAdmin', views.inicialAdmin, name='inicialAdmin'),


]