from django import forms
from django.forms import ModelForm
from .models import Crianca


class CriancaForm(ModelForm):
    class Meta:
        model = Crianca
        fields = "__all__"

        labels = {
            'nome': '',
            'sobrenome': '',
            'data_nascimento': '',
            'sexo': '',
            'CEP': '',
            'endereco': '',
            'alergias': '',
            'nome_responsavel': '',
            'email_resp': '',
            'telefone_resp': '',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de Nascimento: DD/MM/AAAA'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sexo: M/F'}),
            'CEP': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
            'alergias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alergias (opcional)'}),
            'nome_responsavel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Responsável'}),
            'email_resp': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email do responsável'}),
            'telefone_resp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone do Responsável: (XX) XXXXX-XXXX'}),
        }
