from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, PlanoAula
from django_summernote.widgets import SummernoteWidget

# Formulário de Cadastro de Usuário (Mantido)
class CustomUserCreationForm(UserCreationForm):
    nome = forms.CharField(max_length=100, label="Nome Completo")
    email = forms.EmailField(label="E-mail")

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('nome', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# NOVO: Formulário para Criar Plano de Aula
class PlanoAulaForm(forms.ModelForm):
    class Meta:
        model = PlanoAula
        # Campos que o professor preencherá
        fields = ['titulo', 'fk_disciplina', 'fk_serie', 'tema', 'conteudo']
        
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control rounded-pill',
                'placeholder': 'Dê um título ao seu plano'
            }),
            'fk_disciplina': forms.Select(attrs={'class': 'form-select rounded-pill'}),
            'fk_serie': forms.Select(attrs={'class': 'form-select rounded-pill'}),
            'tema': forms.TextInput(attrs={
                'class': 'form-control rounded-pill',
                'placeholder': 'Ex: Figuras de Linguagem'
            }),
            'conteudo': SummernoteWidget(),
        }