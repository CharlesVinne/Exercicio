from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

# Create your views here.

def mostrar_formulario_cadastro(request):
  args = {'msg': ''}
  if request.method == 'POST':
    pessoa = Pessoa()
    pessoa.nome = request.POST.get('nome')
    pessoa.cpf = request.POST.get('cpf')
    pessoa.email = request.POST.get('email')
    pessoa.telefone = request.POST.get('telefone')
    pessoa.genero = request.POST.get('genero')
    pessoa.save()
    return render(request, 'login.html')
  return render(request, 'cadastrar_pessoa.html', args)


def mostrar_pessoas(request):
  pessoas = Pessoa.objects.all()
  return render(request, 'pessoas.html', {'dados': pessoas})


def login(request):
  if request.method == 'POST':
    email_formulario = request.POST.get('email')
    pessoa_banco_dados = Pessoa.objects.filter(email=email_formulario).first()
    if pessoa_banco_dados is not None:
      return mostrar_pessoas(request)
  return render(request, 'login.html', {'msg': 'Ops, não encontramos'})
  return render(request, 'login.html', {'msg': 'olá, bem vindo'})
  
def atualizar(request, id):
  pessoa = Pessoa.objects.get(id=id)
  form = PessoaForm(request.POST or None, instance=pessoa)

  if form.is_valid():
    form.save()
    return redirect(f'../pessoas/')    # o método redirect só redireciona para outra página

  args = {
    'pessoa': pessoa,
    'form': form
  }
  return render(request, 'atualizar.html', args) # o método render renderiza a página, ou seja recarrega a página com a informacao.



