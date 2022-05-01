from django import forms
from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Task
        widgets = {
            "execution_time": forms.DateTimeInput(
                attrs={'class': 'form-control', 'placeholder': 'Select a date and time', 'type': 'datetime'})
        }

