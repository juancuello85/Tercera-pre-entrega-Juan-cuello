from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name= "inicio"),
    path('clientes/', clientes, name="clientes"),    
    path('frutas/', frutas, name="frutas"),    
    path('verduras/', verduras, name="verduras"),    
    path('ganado/', ganado, name="ganado"),
    path('cliente_form/', clienteForm, name="cliente_form"),   
]
