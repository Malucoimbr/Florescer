from django import forms
from django.forms import ModelForm
from .models import Crianca
from .models import Voluntario


class CriancaForm(ModelForm):
    class Meta:
        model = Crianca
        fields = "__all__"

        labels = {
            'nome': '',
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
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de Nascimento: DD/MM/AAAA', 'type': 'date'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sexo: M/F'}),
            'CEP': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
            'alergias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alergias (opcional)'}),
            'nome_responsavel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Responsável'}),
            'email_resp': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email do responsável'}),
            'telefone_resp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone do Responsável: (XX) XXXXX-XXXX'}),
        }

class VoluntarioForm(ModelForm):
    class Meta:
        model = Voluntario
        fields = "__all__"

        labels = {
            'nome': '',
            'data_nascimento': '',
            'sexo': '',
            'CEP': '',
            'endereco': '',
            'email': '',
            'telefone': '',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'volunteer-name', 'placeholder': 'Nome Completo'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de Nascimento: DD/MM/AAAA', 'type': 'date'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sexo: M/F'}),
            'CEP': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone: (XX) XXXXX-XXXX'}),
        }
