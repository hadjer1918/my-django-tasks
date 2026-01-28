# tasks/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','due_date'] 
        widgets ={
            'due_date':forms.DateInput(attrs={'type':'date','class':'bg-transparent border-none outline-none text-slate-500'})
        }