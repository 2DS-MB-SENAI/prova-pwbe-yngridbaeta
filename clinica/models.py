from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


ESPECIALIDADES = [
    ('Cirurgiao', 'Cirurgiao'), 
    ('Oftalmologista', 'Oftalmologista'),
    ('Enfermeiro', 'Enfermeiro'),
    ('CAR', 'Cadiologista')
]

STATUS = [
    ('agendado', 'agendado'),
    ('realizado', 'realizado'),
    ('cancelado', 'cancelado')
]

crm_verificacao = RegexValidator(r'^\d{2}/\d{5}$', 'XX/XXXXX')

class Medico(models.Model):
    nome = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    especialidade = models.CharField(choices=ESPECIALIDADES, max_length=30)
    crm = models.CharField(max_length=30, unique=True, validators=[crm_verificacao])
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    pacientes = models.CharField(max_length=100)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=30)

    def __str__(self):
        return self.pacientes
