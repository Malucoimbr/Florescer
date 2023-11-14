from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Crianca
from .forms import CriancaForm
from .models import Voluntario
from .forms import VoluntarioForm


def login(request):
    return render(request, './index.html')

def telapublica(request):
    return render(request, './index_novo.html')


def cadastrarCrianca(request):
    submit = False
    if request.method == "POST":
        form = CriancaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cadastroCriancas?submit=True')
    else:
        form = CriancaForm()
        if 'submit' in request.GET:
            submit = True
    return render(request, './cadastroCriancas.html', {'form': form, 'submit': submit})

def cadastroVoluntario(request):
    submit = False
    if request.method == "POST":
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cadastroVoluntario?submit=True')
    else:
        form = VoluntarioForm()
        if 'submit' in request.GET:
            submit = True
    return render(request, './cadastroVoluntario.html', {'form': form, 'submit': submit})


def ListarCriancas(request):
    lista_criancas = Crianca.objects.all()
    return render(request, './ListarCriancas.html', {'lista_criancas': lista_criancas})

def listarVoluntario(request):
    lista_voluntario = Voluntario.objects.all()
    return render(request, './listarVoluntario.html', {'lista_voluntario': lista_voluntario})


def inicialAdmin(request):
    return render(request, './inicialAdmin.html')

def doar(request):
    return render(request, './doar.html')