from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

# Create your views here.
def index(request):
    return render(request, 'animales/index.html', {})   
def animal_list(request):
    animal = Animal.objects.all()
    return render(request, 'animales/animal_list.html', {'animal_list': animal})
def protectora_list(request):
    Protectora.objects.all()
    return render(request, 'animales/protectora_list.html', {'protectora_mostrar': Protectora.objects.all()})
def colaborador_list(request):
    Colaborador.objects.all()
    return render(request, 'animales/colaborador_list.html', {'colaborador_mostrar': Colaborador.objects.all()})