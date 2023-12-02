from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),
    path('professores', views.profView, name='professor-lista')
    ]
