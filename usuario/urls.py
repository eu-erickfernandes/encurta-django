from django.urls import path

from usuario.views import login, cadastro, usuarios

app_name = 'usuario'

urlpatterns = [
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('usuarios', usuarios, name='usuarios'),
]