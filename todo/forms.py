from django import forms

# Models
from .models import Todo


class NewTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("description", "priority", "completed", "category")


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("description", "priority", "completed", "category")
