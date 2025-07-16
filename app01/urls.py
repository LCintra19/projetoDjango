#olamundo/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # Mude 'olamundo/' para uma string vazia ''
    path('', ola_mundo),
    path('mensagem/', bem_vindo_template),
    path('frutas/', lista_frutas),
]
