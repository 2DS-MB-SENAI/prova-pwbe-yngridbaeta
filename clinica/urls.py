from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('medicos/', views.listar_medicos, name='listar_medicos'),
    path('consultas/nova/', views.criar_consulta, name='criar_consultas'),
    path('consultas/<int:id>/', views.detalhes_consulta, name='detalhes_consulta'),
]