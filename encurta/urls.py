from django.urls import path

from encurta.views import index

urlpatterns = [
    path('', index)
]