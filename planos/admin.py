from django.contrib import admin
from .models import Usuario, Serie, Disciplina, PlanoAula, Feedback

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'tipo_perfil', 'status_conta')
    search_fields = ('username', 'email')

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status')
    search_fields = ('nome',)

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status')
    search_fields = ('nome',)

@admin.register(PlanoAula)
class PlanoAulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fk_autor', 'fk_disciplina', 'fk_serie')
    search_fields = ('titulo', 'fk_autor__username')
    list_filter = ('fk_disciplina', 'fk_serie')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('plano_aula', 'autor', 'data')
    search_fields = ('plano_aula__titulo', 'autor__username')
