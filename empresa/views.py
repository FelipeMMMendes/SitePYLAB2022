from django.shortcuts import render
from django.http import HttpResponse
from .models import Tecnologias, Empresa
from django.shortcuts import redirect

#Cria views para retornar respostas HTML, no caso, funcoes que sao requisitadas e retornam
#uma pagina
def nova_empresa(request):
    #aqui esta testando as requisicoes do navegador
    if request.method == 'GET':
        #aqui seria um SELECT no banco
        techs = Tecnologias.objects.all()
        #aqui faz com que as tecnologias aparecam visualmente no respectivo campo do site
        return render(request,'nova_empresa.html',{'techs': techs})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        caracteristicas = request.POST.get('caracteristicas')
        tecnologias = request.POST.getlist('tecnologias')
        logo = request.FILES.get('logo')

        #validacoes
        #checa se os campos foram preenchidos
        if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or len(nicho.strip()) == 0 or len(caracteristicas.strip()) == 0 or (not logo)): 
            return redirect('/home/nova_empresa')

        #checa se o tamanho da logo excede 10 MB
        if logo.size > 100_000_000:
            return redirect('/home/nova_empresa')

        #checa se o nicho escolhido esta na lista incluida
        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
            return redirect('/home/nova_empresa')
    