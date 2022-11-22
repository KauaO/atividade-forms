from django.db import models

# Create your models here.
LISTA_SEXO = [
    ('Masculino','Masculino'),
    ('Feminino','Feminino'),
]

LISTA_CURSO = [
    ('Curso Técnico','Curso Técnico'),
    ('Curso Integrado','Curso Integrado'),
]

    
class MiniCursos(models.Model):
    nome = models.CharField(max_length=200)

class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=50)
    email = models.EmailField()
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=150)
    sexo = models.CharField(max_length=150, choices=LISTA_SEXO)
    curso = models.CharField(max_length=150, choices=LISTA_CURSO) 
    minicursos: models.ManyToManyField(MiniCursos, max_length=200)

    def __str__(self) -> str:
        return self.nome