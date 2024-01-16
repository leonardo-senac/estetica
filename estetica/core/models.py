from django.db import models

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class Agenda(models.Model):
    nome = models.CharField(max_length=50)
    data = models.DateField()
    telefone = models.CharField(max_length=14)
    posicao = models.IntegerField()
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

class Servico_dia(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()