from django.shortcuts import render
from django.http import HttpResponse

def ola_mundo(request):
    return HttpResponse("Olá, Mundo no Django!")

def bem_vindo_template(request):
    contexto = {'mensagem': 'Bem-vindo ao Django!'}
    return render(request, 'bemvindo.html', contexto)

def lista_frutas(request):
    frutas = ['Maçã', 'Banana', 'Laranja', 'Abacaxi']
    return render(request, 'lista_frutas.html', {'frutas': frutas})

