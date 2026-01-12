from django.shortcuts import render, redirect
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