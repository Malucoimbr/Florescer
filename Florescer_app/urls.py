from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('cadastroCriancas', views.cadastrarCriancas, name='CadastroCriancas'),
    path('ListarCriancas', views.ListarCriancas, name='ListarCriancas'),
    path('inicialAdmin', views.inicialAdmin, name='inicialAdmin'),
    path('telapublica', views.telapublica, name='telapublica'),

]