# tasks/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-6 py-4 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 dark:focus:ring-indigo-900 outline-none transition-all dark:text-white',
                'placeholder': 'Enter Mission Objective...'
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'w-full px-4 py-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 focus:border-indigo-500 outline-none dark:text-white cursor-pointer'
            }),
            'priority': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 focus:border-indigo-500 outline-none dark:text-white cursor-pointer'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 focus:border-indigo-500 outline-none dark:text-white cursor-pointer'
            }),
        }