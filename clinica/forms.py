from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['pacientes', 'data', 'medico', 'status']

class BuscarConsultaForm(forms.Form):
    pacientes = forms.CharField(max_length=100, required=False, label='Pacientes')
    data = forms.CharField(max_length=100, required=False, label='Data')
    medico = forms.CharField(max_length=100, required=False, label='Medico')
    status = forms.CharField(max_length=100, required=False, label='Status')
