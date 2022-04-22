from nturl2path import url2pathname
from unicodedata import name
from urllib.parse import urlparse
from django.urls import path;
from . import views;


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('biblioteca', views.biblioteca, name='biblioteca'),
    path('biblioteca/crear', views.crear, name='crear'),
    path('biblioteca/editar', views.editar, name='editar'),
]


