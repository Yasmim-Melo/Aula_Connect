from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, PlanoAulaForm  # Adicionado PlanoAulaForm
from .models import PlanoAula

def inicial(request):
    """Renderiza a página inicial pública."""
    return render(request, 'planos/inicial.html')

def registrar(request):
    """Lógica de cadastro de novos usuários."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'planos/cadastro.html', {'form': form})

@login_required
def meus_planos(request):
    """Exibe os planos de aula do professor logado."""
    planos = PlanoAula.objects.filter(fk_autor=request.user).order_by('-id')
    
    return render(request, 'planos/meus_planos.html', {
        'titulo_pagina': 'Meus Planos de Aula',
        'planos': planos
    })

@login_required
def criar_plano(request):
    """
    Lógica para a tela de criação de novo plano.
    Processa o formulário e salva o autor automaticamente.
    """
    if request.method == 'POST':
        form = PlanoAulaForm(request.POST)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.fk_autor = request.user  # Define o autor como o usuário logado
            plano.save()
            return redirect('meus_planos')
    else:
        form = PlanoAulaForm()
    
    return render(request, 'planos/criar_plano.html', {'form': form})

@login_required
def modelos_planos(request):
    """Exibe modelos globais do sistema."""
    return render(request, 'planos/modelos_planos.html')