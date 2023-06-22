from encurta.models import Link, Url

def encurta_link(request):
    url = request.POST.get('url')
    url_model = Url.objects.get_or_create(url= url)[0]

    usuario = request.user if request.user.id else None

    novo_link = Link()

    novo_link.url = url_model
    novo_link.usuario = usuario

    novo_link.save()

    return novo_link