from django.contrib import admin
from .models import Aluno,Curso,Campus,Disciplina

# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display=('nome','email','data_nascimento')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin): 
    list_display=('nome','carga_horaria')

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin): 
    list_display=('nome','nome_cidade')
