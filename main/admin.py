from django.contrib import admin
from main.models import *
from main.forms import *
# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = { 'nome', 'email', 'sexo', 'curso', 'minicurso'}
    search_fields = ('nome')
    list_filter = {'curso'}


   



admin.site.register(AlunoAdmin, Aluno)