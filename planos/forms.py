from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    nome = forms.CharField(max_length=100, label="Nome Completo")
    email = forms.EmailField(label="E-mail")

    class Meta(UserCreationForm.Meta):
        model = Usuario

        fields = UserCreationForm.Meta.fields + ('nome', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica a classe do Bootstrap em todos os campos
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'