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

def tirar_dados(request):
    from datetime import datetime
    from random import randint
    
    valor_de_dado = randint(1 ,6)
    
    if valor_de_dado == 6:
        mensaje = f"Sacaste {valor_de_dado}. Ganaste! "
    else:
        mensaje = f"Sacaste {valor_de_dado}. Perdiste! Presiona F5 para otro intento."
        
    datos = {
        'titulo' : "Juego del dodo",
        'mensaje' : mensaje,
        'fecha' : datetime.now().now,        
    }
    
    return render(request, 'principal/dados.html', context=datos)