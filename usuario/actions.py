# TODO:
# -Validar

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.http import HttpRequest
from typing import Tuple, List

def cadastrar_usuario(request: HttpRequest):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    nome_usuario = request.POST.get('nome-usuario')
    senha = request.POST.get('senha')

    print(nome, email, nome_usuario, senha)

    usuario = User.objects.create_user(
        first_name= nome,
        email= email,
        username= nome_usuario,
        password= senha
    )

    login(request, usuario)

    return usuario


def entrar(request: HttpRequest):
    nome_usuario = request.POST.get('nome-usuario')
    senha = request.POST.get('senha')

    usuario = authenticate(username= nome_usuario, password= senha)

    if usuario:
        login(request, usuario)
    
    return usuario

def sair(request: HttpRequest):
    logout(request)
