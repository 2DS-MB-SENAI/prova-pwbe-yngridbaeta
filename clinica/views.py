from django.shortcuts import render, redirect, get_list_or_404
from .models import Medico, Consulta


#listar todos os medicos cadastrados
def listar_medicos(request):
    medicos = []

    medicos = Medico.objects.all()
    

