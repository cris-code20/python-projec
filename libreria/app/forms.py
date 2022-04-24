from dataclasses import field
from pyexpat import model
from django import forms
from .models import Libro


class From(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'