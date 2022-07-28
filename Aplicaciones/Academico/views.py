from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.
def home(request):
    cursos=Curso.objects.all()
    #messages.success(request,'¡Cursos encontrados existosamente!')
    return render(request,'gestionCursos.html',{"cursos":cursos})

def registrarCurso(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    creditos=request.POST['creditos']
    
    curso=Curso.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
    #messages.success(request,'¡Curso agregado existosamente!')
    return redirect('/')

def eliminarCurso(request,codigo):
    curso=Curso.objects.filter(codigo=codigo).delete()
    #messages.success(request,'¡Curso eliminado existosamente!')
    return redirect('/')

def obtenerCurso(request,codigo):
    curso=Curso.objects.filter(codigo=codigo).get()
    return render(request,'edicionCurso.html', {"curso":curso})

def editarCurso(request,codigo):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    creditos=request.POST['creditos']
    curso=Curso.objects.filter(codigo=codigo).update(nombre=nombre,creditos=creditos)
    #messages.success(request,'¡Curso actualizado existosamente!')
    return redirect('/')
