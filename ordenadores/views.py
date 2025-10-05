from django.shortcuts import render
from .models import Procesador, Ram, Grafica

# Create your views here.
def index(request):
    return render(request, 'ordenadores/index.html', {})   
def procesador_list(request):
    procesador = Procesador.objects.all()
    return render(request, 'ordenadores/procesador_list.html', {'procesador_list': procesador})
def ram_list(request):
    ram = Ram.objects.all()
    return render(request, 'ordenadores/ram_list.html', {'ram_list': ram})
def grafica_list(request):
    grafica = Grafica.objects.all()
    return render(request, 'ordenadores/grafica_list.html', {'grafica_list': grafica})