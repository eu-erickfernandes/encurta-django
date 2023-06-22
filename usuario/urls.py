from django.urls import path

from usuario.views import login, cadastro, usuarios, logout, meus_links

app_name = 'usuario'

urlpatterns = [
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('usuarios', usuarios, name='usuarios'),
    path('meus-links', meus_links, name='meus-links'),
]