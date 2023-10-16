from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Crianca
from .forms import CriancaForm


def home(request):
    return render(request, './index.html')


def cadastrarCriancas(request):
    submit = False
    if request.method == "POST":
        form = CriancaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cadastroCriancas?cadastro=True')
    else:
        form = CriancaForm()
        if 'cadastro' in request.GET:
            submit = True
    return render(request, './cadastroCriancas.html', {'form': form, 'submit': submit})


def ListarCriancas(request):
    return render(request, './ListarCriancas.html')


def inicialAdmin(request):
    return render(request, './inicialAdmin.html')
