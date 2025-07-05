from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description=forms.CharField(label="descripcion de la tarea", widget=forms.Textarea)
    project = forms.ModelChoiceField(queryset=Project.objects.all(), label="Proyecto")


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Projecto", max_length=200)