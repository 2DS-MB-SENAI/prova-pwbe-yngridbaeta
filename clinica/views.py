from django.shortcuts import render, redirect, get_list_or_404
from .models import Medico, Consulta
from .forms import ConsultaForm


#listar todos os medicos cadastrados
def listar_medicos(request):

    medicos = Medico.objects.all()
    
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos})

def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ConsultaForm()
    return render(request, 'clinica/form_consulta.html', {'form': form})
