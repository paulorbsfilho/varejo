from django.db import models


# Create your models here.


class Cliente(models.Model):
    PARTICIPANTE = (
        ('SIM', 'Sim'),
        ('NAO', 'Não')
    )
    nome = models.CharField('Nome', max_length=50, default='Cliente')
    clube_fidelidade = models.CharField(max_length=3, choices=PARTICIPANTE, default='SIM')
    pontos_de_fidelidade = models.IntegerField('Pontos')


class Compra(models.Model):
    valor_total = models.FloatField('Valor da compra')
    pontos_da_compra = models.IntegerField('Pontos ganhos nesta compra')
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)


    def qtd_itens(self):
        return len(self.itens.all())


class ItemCompra(models.Model):
    nome_item = models.CharField('Item')
    valor = models.FloatField('Valor unitario')
    quantidade = models.IntegerField('Quantidade')
    compra = models.ForeignKey('Compra', related_name="itens", on_delete=models.CASCADE)
