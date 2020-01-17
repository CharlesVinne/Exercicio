from django.shortcuts import render
<<<<<<< HEAD
# Create your views here.
=======
>>>>>>> 5f99d31c911f33de409b837568c6084c949967be
from .models import Pessoa

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
<<<<<<< HEAD


def mostrar_pessoas(request):
  pessoas = Pessoa.objects.all()

  args = {'mostrar_pessoas': mostrar_pessoas}

=======

def mostrar_pessoas(request):
  pessoas = Pessoa.objects.all()
>>>>>>> 5f99d31c911f33de409b837568c6084c949967be
  return render(request, 'pessoas.html', {'dados': pessoas})

def login(request):
  if request.method == 'POST':
    email_formulario = request.POST.get('email')
    pessoa_banco_dados = Pessoa.objects.filter(email=email_formulario).first()
    if pessoa_banco_dados is not None:
<<<<<<< HEAD
      args = {
        'pessoa': pessoa_banco_dados
      }
=======
>>>>>>> 5f99d31c911f33de409b837568c6084c949967be
      return mostrar_pessoas(request)
    return render(request, 'login.html', {'msg': 'Ops, não encontramos'})

  return render(request, 'login.html', {'msg': 'seja bem vindo'})