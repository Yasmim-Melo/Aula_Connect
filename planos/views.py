from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Importante para proteção de telas
from .forms import CustomUserCreationForm

def inicial(request):
    return render(request, 'planos/inicial.html')

def registrar(request):
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
    """Lógica: Filtra planos onde o autor é o professor logado."""
    # Exemplo de lógica futura: 
    # planos = PlanoAula.objects.filter(professor=request.user).order_by('-data_criacao')
    return render(request, 'planos/meus_planos.html', {
        'titulo_pagina': 'Meus Planos de Aula'
    })

@login_required
def modelos_planos(request):
    """Lógica: Exibe modelos pré-definidos pelo sistema (globais)."""
    return render(request, 'planos/modelos_planos.html')