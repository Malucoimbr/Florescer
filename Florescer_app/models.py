from django.db import models

class Crianca(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=120)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=5)
    CEP = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    alergias = models.TextField(blank = True)
    nome_responsavel = models.CharField(max_length=200)
    email_resp = models.EmailField()
    telefone_resp = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
