from django.shortcuts import render

# Create your views here.
from .models import *
from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html', {})


class DescontoValor():


class Requisito_Preco():

    def cliente_elegivel(self):
        elegivel = False
        lista_compras = Compra.objects.all()
        for compra in lista_compras:
            if (compra.valor_total == 1000):
                elegivel = True
        return elegivel


class Requisito_Pontos():

    def cliente_elegivel(self):
        elegivel = False
        lista_compras = Compra.objects.all()
        for compra in lista_compras:
            if (compra.cliente.PARTICIPANTE):
                if (compra.cliente.pontos_de_fidelidade == 1000):
                    elegivel = True
        return elegivel


class Requisito_Quantidade():

    def cliente_elegivel(self):
        elegivel = False
        lista_compras = Compra.objects.all()
        for compra in lista_compras:
            if (compra.qtd_itens()>=20):
                elegivel = True
        return elegivel


class Escolha_desconto():



class DescontoFidelidade():
    if()

#class DescontoQuantidade():

