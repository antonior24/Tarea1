from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('procesadores/', views.procesador_list, name='procesador_list'),
    path('ram/', views.ram_list, name='ram_list'),
    path('graficas/', views.grafica_list, name='grafica_list'),
]