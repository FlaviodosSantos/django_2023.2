from django.shortcuts import render
import requests  # faz requisições HTTP


def index(request):
    api = "http://127.0.0.1:3000/books/"
    requisicao = requests.get(api)

    try:
        lista = requisicao.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "livros": dicionario
    }

    return render(request, "index.html", contexto)
