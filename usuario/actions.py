# TODO:
# -Validar

from django.http import HttpRequest
from typing import Tuple, List
from django.contrib.auth.models import User

def cadastrar_usuario(request: HttpRequest) -> Tuple[User, List]:
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

    # usuario.save()

    print('cheguei aqui', usuario)