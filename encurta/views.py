from django.shortcuts import render, redirect, get_object_or_404
from setup.settings import BASE_DIR

from encurta.actions import encurta_link
from encurta.models import Link, Url

# Create your views here.
def index(request):
    base = BASE_DIR
    links_gerados = Link.objects.all()
    qtd_links_gerados = links_gerados.count()

    urls = Url.objects.all()
    qtd_urls_geradas = urls.count()

    if request.method == 'POST':
        encurta_link(request)

        return redirect('/')

    return render(request, 'encurta/index.html',{
        'links_gerados': links_gerados, 
        'qtd_links_gerados': qtd_links_gerados,
        'qtd_urls_geradas': qtd_urls_geradas,
        'urls': urls  
    })

def link(request, id_link):
    link = get_object_or_404(Link, id= id_link)

    link.qtd_acessos += 1
    link.save()

    return redirect(link.url.url)