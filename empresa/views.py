from django.shortcuts import render
from .forms import EmpresaForm
from .models import Empresa

# Create your views here.

def cadastro(request):

    form = EmpresaForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args['msg',] = 'Cadastro Realizado Com Sucesso'
    return render(request, 'cadastro.html', args)

def atualizar(request, id):
    empresa = empresa.objects.get(id=id)
    form = EmpresaForm(request.POST or None, empresa)

    if form.is_valid():
        form.save()
        return redirect(f'../atualizar/{atualizar.id}')

    args = {
        'empresa':empresa,
        'form':form
    }
    return render(request, 'atualizar.html', args)

def deletar(request):
    empresa = Empresa.objects.get(id=id)
    args = {
        'empresa': empresa
    }
    empresa.delete()
    return render(request, 'deletar.html', args)
