from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fiels = ['nome', 'especialidade', 'crm', 'email']


class BuscarConsultaForm(forms.Form):
    nome = forms.CharField(max_length=100, required=False, label='Nome')
    especialidade = forms.CharField(max_length=100, required=False, label='especialidade')
