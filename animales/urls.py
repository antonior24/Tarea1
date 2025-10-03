from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animales/', views.animal_list, name='animal_list'),
    path('protectora/', views.protectora_list, name='protectora_list'),
    path('colaboradores/', views.colaborador_list, name='colaborador_list'),
]