from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models

#aqui definimos as tabelas SQL (O computador pega o codigo em Python e 'traduz' pra SQL)
#cada classe é uma tabela
#a tabela tecnologias é feita para guardar os dados sobre as tecnologias que tais empresas
#usam, nisso temos uma relação de muitos pra muitos, já que uma tecnologia pode ser 
# usada por várias empresas e uma empresa pode ter várias tecnologias
class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    #metodo para auxiliar na impressao da tabela
    def __str__(self):
        return self.tecnologia

class Empresa(models.Model):
    #cria uma tupla para limitar as opcoes de escolha do usuario relacionadas ao nicho
    choices_nicho_mercado = (
        ('M','Marketing'),
        ('T','Tecnologia'),
        ('G','Games')    
    )
    #aqui definimos as colunas, por exemplo, temos nome, do tipo char com tamanho máximo de 30
    logo = models.ImageField(upload_to="logo_empresa",null=True)#null=True faz com que não seja obrigatório
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    #por conta da relação entre as tabelas, usa o ManyToMany 
    tecnologias = models.ManyToManyField(Tecnologias)
    endereco = models.CharField(max_length=30)
    caracteristica_empresa = models.TextField()#textfield armazena textos maiores
    nicho_mercado = models.CharField(max_length=3,choices=choices_nicho_mercado)
    #o argumento choices faz com que o usuario tenha que escolher alguma opcao

    def __str__(self):
        return self.nome

class Vagas(models.Model):
    choices_experiencia = (
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )
    
    #para vagas, temos uma relacao de um para muitos com as empresas, afinal
    #uma empresa pode ter varias vagas, mas uma vaga só pode ter uma empresa
    #nisso, usamos o ForeignKey, e o on_delete é caso deletem a empresa, o
    #DO_NOTHING garante que não façam nada na vaga
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(Tecnologias, related_name='estudar')


    def __str__(self):
        return self.titulo        