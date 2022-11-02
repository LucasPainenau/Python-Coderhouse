from django.shortcuts import render
from appcoder.models import Curso

# Create your views here.

def listado_cursos(request):
    cursos = Curso.objects.all
    