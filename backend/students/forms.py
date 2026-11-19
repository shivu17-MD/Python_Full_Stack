from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=[
            'name',
            'email',
            'age',
            'department'
        ]

    #   explain
    #   forms.Form -create a Django forms
    