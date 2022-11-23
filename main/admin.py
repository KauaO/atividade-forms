from django.contrib import admin
from main.models import *
from main.forms import *
# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = ( 'nome', 'email', 'sexo')
    search_fields = (['nome'])
    list_filter = (['curso'])


   

admin.site.register(MiniCursos)
admin.site.register(Aluno, AlunoAdmin)