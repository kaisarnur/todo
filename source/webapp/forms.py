from django import forms
from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Task
