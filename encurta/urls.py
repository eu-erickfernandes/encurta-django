from django.urls import path

from encurta.views import index, link

app_name = 'encurta'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id_link>', link, name='link'),
]