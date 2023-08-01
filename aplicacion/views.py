from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def clientes(request):
    return render(request, "aplicacion/clientes.html")

def frutas(request):
    return render(request, "aplicacion/frutas.html")

def verduras(request):
    return render(request, "aplicacion/verduras.html")

def ganado(request):
    return render(request, "aplicacion/ganado.html")

def clienteForm(request):
    return render(request, "aplicacion/clienteForm.html")

