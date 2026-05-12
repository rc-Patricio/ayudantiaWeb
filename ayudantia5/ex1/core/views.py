import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from pathlib import Path


def inicio(request):
    return render(request, 'inicio.html')

def sesion(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'sesion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

def cat1(request):
    ruta = Path(__file__).resolve().parent / "data" / "cat1" / "productos.json"

    with open(ruta, encoding="utf-8") as archivo:
        lista = json.load(archivo)

    return render(request, "cat1.html", {
        "productos": lista
    })

def cat2(request):

    ruta = Path(__file__).resolve().parent / "data" / "cat2" / "productos.json"

    with open(ruta, encoding="utf-8") as archivo:
        lista = json.load(archivo)

    return render(request, "cat2.html", {
        "productos": lista
    })

def nosotros(request):
    return render(request, 'inicio.html')

def registroInicio(request):
    return render(request, 'registroInicio.html')
