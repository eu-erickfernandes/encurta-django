from django.db import models

class Url(models.Model):
    url = models.CharField(max_length= 100)

    def get_links(self):
        return Link.objects.filter(url= self)
    
    def get_qtd_links(self):
        return Link.objects.filter(url= self).count()

class Link(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    qtd_acessos = models.IntegerField(default= 0)
