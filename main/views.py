from .models import Aluno, Professor
from django.shortcuts import render

def alunoView(request):
    alunos_list = Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list': alunos_list})

def profView(request):
    professores_list = Professor.objects.all()
    return render(request, 'main/professores.html', {'professores_list': professores_list})