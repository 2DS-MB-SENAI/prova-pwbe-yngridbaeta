from django.shortcuts import render, redirect, get_list_or_404
from .models import Medico, Consulta
from .forms import ConsultaForm, BuscarConsultaForm
from django.contrib import messages


def index(request):
    return render(request, 'clinica/base.html')

#listar todos os medicos cadastrados
def listar_medicos(request):

    medicos = Medico.objects.all()
    
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos})

def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Consulta criada')
        # return redirect('clinica/base.html')
    else:
        form = ConsultaForm()
        messages.error(request, 'erro ao criar consulta')
    return render(request, 'clinica/form_consulta.html', {'form': form})


def detalhes_consulta(request):
    form = BuscarConsultaForm(request.GET)
    consulta = get_list_or_404(Consulta, id=id)
    return render(request, 'clinica/detalhes_consulta.html', {'consulta': consulta})