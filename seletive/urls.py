#nesse arquivo fazemos o roteamento da aplicação
from django.contrib import admin
from django.urls import path, include

#essa urlpatterns serve para definir onde cada endereço leva
urlpatterns = [
    path('admin/', admin.site.urls),
    #esse trecho faz com que quando o endereço estiver em home/, ele leve para as empresas
    path('home/', include('empresa.urls'))
]
