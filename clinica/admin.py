from django.contrib import admin
from .models import Medico, Consulta

admin.site.register(Consulta),
admin.site.register(Medico)
