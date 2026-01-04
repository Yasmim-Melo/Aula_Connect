from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    class TipoPerfil(models.TextChoices):
        PROFESSOR = 'professor', 'Professor'
        ALUNO = 'aluno', 'Aluno'

    class StatusConta(models.TextChoices):
        ATIVA = 'ativa', 'Ativa'
        INATIVA = 'inativa', 'Inativa'

    biografia = models.TextField(blank=True, null=True)
    cota_ia_diaria = models.IntegerField(default=0)
    tipo_perfil = models.CharField(max_length=20, choices=TipoPerfil.choices, default=TipoPerfil.ALUNO)
    status_conta = models.CharField(max_length=20, choices=StatusConta.choices, default=StatusConta.ATIVA)

class Serie(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

class PlanoAula(models.Model):
    titulo = models.CharField(max_length=200)
    tema = models.TextField()
    metodologia = models.TextField()
    objetivos = models.TextField()
    conteudo = models.TextField()
    duracao = models.DurationField()
    fk_autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='planos_autor')
    fk_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    fk_serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    fk_origem = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='planos_derivados')

class Feedback(models.Model):
    plano_aula = models.ForeignKey(PlanoAula, on_delete=models.CASCADE, related_name='feedbacks')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='feedbacks_autor')
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
