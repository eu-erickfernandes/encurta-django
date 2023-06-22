from django.shortcuts import render

from usuario.actions import cadastrar_usuario

# Create your views here.
def cadastro(request):
    template_name = 'usuario/cadastro.html'

    if request.method == 'POST':
        novo_usuario = cadastrar_usuario(request)



    return render(request, template_name)


def login(request):
    template_name = 'usuario/login.html'

    return render(request, template_name)


def usuarios(request):
    template_name = 'usuario/usuarios.html'

    return render(request, template_name)