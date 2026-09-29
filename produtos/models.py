from django.db import models

class Fazenda(models.Model):
    nome = models.CharField(max_length=120)
    produtor = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.nome} ({self.cidade}/{self.uf})"
class Lavoura(models.Model):
    OPCOES_CULTURA = [
        ('SOJA', 'Soja'),
        ('MILHO', 'Milho'),
        ('ALGODAO', 'Algodão'),
        ('CAFE', 'Café'),
        ('OUTRO', 'Outro'),
    ]
    fazenda = models.ForeignKey(Fazenda, on_delete=models.CASCADE, related_name='lavouras')
    tipo_cultura = models.CharField(max_length=20, choices=OPCOES_CULTURA, default='SOJA')
    area_em_hectares = models.DecimalField(max_digits=8, decimal_places=2)
    latitude = models.FloatField()
    longitude = models.FloatField()
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_cultura} - {self.fazenda.nome}"