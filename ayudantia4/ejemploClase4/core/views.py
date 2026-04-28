import json
from django.shortcuts import render

from pathlib import Path


def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, "nosotros.html")

def alumnos(request):

    ruta = Path(__file__).resolve().parent / "data" / "alumnos.json"

    with open(ruta, encoding="utf-8") as archivo:
        lista = json.load(archivo)

    return render(request, "alumnos.html", {
        "alumnos": lista
    })