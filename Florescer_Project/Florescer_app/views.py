from django.shortcuts import render

def home (request):
    return render(request, './index.html')

def cadastrarCriancas(request):
    return render(request, './cadastroCriancas.html')

def ListarCriancas(request):
    return render(request, './ListarCriancas.html')

def inicialAdmin(request):
    return render(request, './inicialAdmin.html')



