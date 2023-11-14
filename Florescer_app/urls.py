from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('cadastroCriancas', views.cadastrarCrianca, name='CadastroCriancas'),
    path('ListarCriancas', views.ListarCriancas, name='ListarCriancas'),
    path('cadastroVoluntario', views.cadastroVoluntario, name='cadastroVoluntario'),
    path('listarVoluntario', views.listarVoluntario, name='listarVoluntario'),
    path('inicialAdmin', views.inicialAdmin, name='inicialAdmin'),
    path('', views.telapublica, name='telapublica'),
    path('doar', views.doar, name='doar'),
]