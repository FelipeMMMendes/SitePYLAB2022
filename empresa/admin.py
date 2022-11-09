from django.contrib import admin
from .models import Tecnologias, Empresa, Vagas
# Register your models here.

#serve para cadastrar as empresas e tecnologias na parte de admin do site
admin.site.register(Tecnologias)
admin.site.register(Empresa)
admin.site.register(Vagas)