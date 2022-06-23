from django import forms
from django.forms import ModelForm
from .models import Task, Plant

class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ('plant_name', 'plant_species')

        widgets = {
            'plant_name':forms.TextInput(attrs={'class':'form-control'}),
        }

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('task_title', 'task_note', 'task_plant', 'task_user')


