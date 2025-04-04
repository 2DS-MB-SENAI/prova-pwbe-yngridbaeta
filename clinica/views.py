from django.shortcuts import render, redirect, get_list_or_404
from .models import Medico, Consulta


#listar todos os medicos cadastrados
def listar_medicos(request):


    medicos = Medico.objects.all()
    
    return render(request, 'listar_medicos.html', {'medicos': medicos})

