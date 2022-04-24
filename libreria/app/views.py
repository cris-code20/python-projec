from unicodedata import name;
from django.shortcuts import render, redirect;
from  django.http import HttpResponse;
from  .models import Libro  ;
from .forms import  From;

# Create your views here.

# def precentacionWeb(request):
#     return HttpResponse("<h1>Bienbenido putin</h1>")

def inicio(request):
    return render(request,'web-site/inicio.html')

def nosotros(request):
    return render(request,'web-site/nosotros.html')


def biblioteca(request):
    biblioteca = Libro.objects.all()
    # print(biblioteca)
    return render(request, 'biblioteca/index.html', {'biblioteca': biblioteca })


def crear(request):
    formulario = From(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('biblioteca')
    return render(request, "biblioteca/crear.html", {'formulario': formulario})


def editar(request):
    nota = Libro.objects.get(id=id)
    formulario = From(request.POST or None, request.FILES or None, instance=nota)
    return render(request, "biblioteca/editar.html", {'formulario': formulario})


def eliminar(request, id):
    nota = Libro.objects.get(id=id)
    nota.delete()
    return redirect('biblioteca')
    
