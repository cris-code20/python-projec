from nturl2path import url2pathname
from unicodedata import name
from urllib.parse import urlparse
from django.urls import path;
from . import views;


urlpatterns = [
    path('', views.precentacionWeb, name='precentacionWeb'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('biblioteca', views.biblioteca, name='biblioteca'),
]


