from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.CharField(max_length= 100)
    qtd_acessos = models.IntegerField(default= 0)