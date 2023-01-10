from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .forms import TransacaoForm

import datetime

# Create your views here.


def home(request):
    data = {}
    data['transacoes'] = ["t1", 't2', 't3']
    data['now'] = datetime.datetime.now()
    # html = f"<html><body>It's now {now} </body></html>"
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacao'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    return render(request, 'contas/form.html', {'form': form})


def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
