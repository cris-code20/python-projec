from django.shortcuts import render;
from  django.http import HttpResponse;


# Create your views here.

# def precentacionWeb(request):
#     return HttpResponse("<h1>Bienbenido putin</h1>")

def inicio(request):
    return render(request,'web-site/inicio.html')

def nosotros(request):
    return render(request,'web-site/nosotros.html')


def biblioteca(request):
    return render(request, 'biblioteca/index.html')


