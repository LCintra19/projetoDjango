#olamundo/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # Mude 'olamundo/' para uma string vazia ''
    path('', lista_livros),
]
