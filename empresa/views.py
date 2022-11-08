from django.shortcuts import render
from django.http import HttpResponse

#Cria views para retornar respostas HTML, no caso, funcoes que sao requisitadas e retornam
#uma pagina
def nova_empresa(request):
    return render(request,'nova_empresa.html')