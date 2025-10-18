from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request):
    return HttpResponse ("Hola")

def saludar2 (request, nombre:str, apellido:str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse (f"Hola {nombre} {apellido}")

def index(request):
    from datetime import datetime
    año_actual = datetime.now().year
    contexto = {"año":año_actual}
    return render (request, "principal/index.html", contexto)