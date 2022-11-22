from django import forms
from main.models import *

class AlunoForm(forms.ModelForm):
    class Meta:
        model=Aluno
        fields= '__all__'

        widgets = {
            'minicursos': forms.CheckboxSelectMultiple(),
            'sexo': forms.RadioSelect(),
            'data_nascimento': forms.TimeInput(attrs={'type': 'date'}),
        }


