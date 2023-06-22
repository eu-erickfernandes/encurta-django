from django.contrib.auth.models import User 

from django.shortcuts import render, redirect

from encurta.models import Link

from usuario.actions import cadastrar_usuario, entrar, sair

# Create your views here.
def cadastro(request):
    template_name = 'usuario/cadastro.html'

    if request.method == 'POST':
        novo_usuario = cadastrar_usuario(request)



    return render(request, template_name)


def login(request):
    template_name = 'usuario/login.html'

    if request.POST:
        entrar(request)

    return render(request, template_name)

def logout(request):
    sair(request)

    return redirect('/')


def usuarios(request):
    print(request.user)
    template_name = 'usuario/usuarios.html'

    usuarios = User.objects.all().order_by('first_name')

    return render(request, template_name, {
        'usuarios': usuarios
    })


def meus_links(request):
    template_name = 'usuario/meus-links.html'

    links = Link.objects.filter(usuario= request.user)

    return render(request, template_name, {
        'links': links
    })