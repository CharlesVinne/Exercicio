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
def deletar(request):
    empresa = Empresa.objects.get(id=id)
    args = {
        'empresa': empresa
    }
    empresa.delete()
    return render(request, 'deletar.html', args)