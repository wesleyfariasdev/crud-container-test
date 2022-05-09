from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.name
