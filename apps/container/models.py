from django.db import models
from apps.cliente.models import Client


class Container(models.Model):
    TYPE_CONTAINER_CHOICES = (
        ('20', '20'),
        ('40', '40')
    )
    STATUS_CONTAINER_CHOICES = (
        ('Cheio', 'Cheio'),
        ('Vazio', 'Vazio'),
    )
    CATEGORY_CONTAINER_CHOICES = (
        ('Importação', 'Importação'),
        ('Exportação', 'Exportação'),
    )
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    container_number = models.CharField(max_length=11)
    type = models.CharField(max_length=2, choices=TYPE_CONTAINER_CHOICES)
    status = models.CharField(max_length=5, choices=STATUS_CONTAINER_CHOICES)
    category = models.CharField(max_length=10, choices=CATEGORY_CONTAINER_CHOICES)

    def __str__(self):
        return self.container_number

