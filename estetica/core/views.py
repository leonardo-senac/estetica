from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def cadastro_servico(request):
    if request.method == 'POST':
       form = FormServico(request.POST)
       if form.is_valid():
            form.save()
    form = FormServico()
    context = {
        'form': form,
    }
    return render(request, 'cadastro_servico.html', context)

def servico_dia(request):
    if request.method == 'POST':
       form = FormServicoDia(request.POST)
       if form.is_valid():
            form.save()
    form = FormServicoDia()
    context = {
        'form': form,
    }
    return render(request, 'servico_dia.html', context)

def regulamento(request):
     return render(request, 'regulamento.html')

def pagina_servico(request):
     return render(request, 'pagina_servico.html')

def local(request):
     return render(request, 'local.html')

def listagem(request):
     return render(request, 'listagem.html')