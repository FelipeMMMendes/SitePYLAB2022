#nesse arquivo fazemos o roteamento da aplicação
from django.urls import path
from . import views

#essa urlpatterns serve para definir onde cada endereço leva
urlpatterns = [
    path('nova_empresa/', views.nova_empresa, name="nova_empresa")
]