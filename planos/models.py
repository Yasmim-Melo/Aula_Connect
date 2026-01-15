from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    class TipoPerfil(models.TextChoices):
        PROFESSOR = 'professor', 'Professor'
        COORDENADOR = 'coordenador', 'Coordenador'

    class StatusConta(models.TextChoices):
        ATIVA = 'ativa', 'Ativa'
        INATIVA = 'inativa', 'Inativa'

    # Configuração de Login por E-mail
    email = models.EmailField('E-mail', unique=True)
    
    biografia = models.TextField(blank=True, null=True)
    cota_ia_diaria = models.IntegerField(default=0)
    
    # Definindo Professor como padrão para evitar erros
    tipo_perfil = models.CharField(
        max_length=20, 
        choices=TipoPerfil.choices, 
        default=TipoPerfil.PROFESSOR
    )
    status_conta = models.CharField(
        max_length=20, 
        choices=StatusConta.choices, 
        default=StatusConta.ATIVA
    )

    # Faz o Django usar o E-mail para autenticação
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Serie(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

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

    def __str__(self):
        return self.titulo

class Feedback(models.Model):
    plano_aula = models.ForeignKey(PlanoAula, on_delete=models.CASCADE, related_name='feedbacks')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='feedbacks_autor')
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)