from nturl2path import url2pathname
from unicodedata import name
from urllib.parse import urlparse
from django.urls import path;
from . import views;

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('biblioteca', views.biblioteca, name='biblioteca'),
    path('biblioteca/crear', views.crear, name='crear'),
    path('biblioteca/editar', views.editar, name='editar'),
    path('biblioteca/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.editar, name='eliminar'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


