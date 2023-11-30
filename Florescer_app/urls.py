from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('cadastroCriancas', views.cadastrarCrianca, name='CadastroCriancas'),
    path('cadastroFinanceiro', views.cadastrarRegistroFinanceiro, name='cadastroFinanceiro'),
    path('ListarCriancas', views.ListarCriancas, name='ListarCriancas'),
    path('listarFinancas', views.listarFinancas, name='listarFinancas'),
    path('cadastroVoluntario', views.cadastroVoluntario, name='cadastroVoluntario'),
    path('listarVoluntario', views.listarVoluntario, name='listarVoluntario'),
    path('inicialAdmin', views.inicialAdmin, name='inicialAdmin'),
    path('visualizarDash', views.visualizarDash, name='visualizarDash'),
    path('', views.telapublica, name='telapublica'),
    path('doar', views.doar, name='doar'),
]