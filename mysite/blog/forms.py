from dataclasses import fields
from tkinter import Widget
from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        } 
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        #self.fields['title'].widget.attrs.update(
        #    {'class': 'input'}
        #)
