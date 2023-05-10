from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Campus(models.Model):
    nome = models.CharField(max_length=100)
    nome_cidade = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    data_nascimento = models.DateField()
    campus = models.ForeignKey(Campus,on_delete=models.CASCADE)    
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    disciplina = models.ManyToManyField(Disciplina)
