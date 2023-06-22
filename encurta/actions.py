from encurta.models import Link, Url

def encurta_link(request):
    post = request.POST

    url = post['url']

    novo_link = Link()
    print(novo_link)

    url_model = Url.objects.get_or_create(url= url)[0]

    novo_link.url = url_model

    print(url_model)

    novo_link.save()