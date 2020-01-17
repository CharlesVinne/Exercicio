from django.db import models

# Create your models here.

class Empresa(models.Model):
    portes = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    )

    segmentos = (
        ('T','Tecnologia'),
        ('C','Construção'),
        ('I','Industrial'),
        ('E','Engenharia'),
    )

    nome = models.CharField(max_length=255,verbose_name='Nome')
    cnpj = models.CharField(max_length=12,verbose_name='CNPJ')
    endereco = models.CharField(max_length=255,verbose_name='Endereço')
    porte = models.CharField(max_length=255,verbose_name='Porte', choices=portes)
    dono = models.CharField(max_length=255,verbose_name='Dono')
    data_abertura = models.DateField(verbose_name='Data abertura')
    telefone = models.IntegerField(max_length=20,verbose_name='Telefone')
    email = models.EmailField(max_length=100,verbose_name='Email')
    segmento = models.CharField(max_length=255,verbose_name='Segmento', choices=segmentos)

    def __str__(self):
        return self.nome
    