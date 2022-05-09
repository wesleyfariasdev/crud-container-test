from django.core.exceptions import ValidationError
from django.db import models
from apps.container.models import Container


class Movement(models.Model):
    TYPE_MOVEMENT_CHOICES = (
        ('Embarque', 'Embarque'),
        ('Descarga', 'Descarga'),
        ('Gate In', 'Gate In'),
        ('Gate Out', 'Gate Out'),
        ('Reposicionamento', 'Reposicionamento'),
        ('Pessagem', 'Pessagem'),
        ('Scanner', 'Scanner'),
    )
    container = models.ForeignKey(Container, on_delete=models.DO_NOTHING)
    type_movement = models.CharField(max_length=16, choices=TYPE_MOVEMENT_CHOICES)
    initial_date = models.DateTimeField()
    finish_date = models.DateTimeField()

    def __str__(self):
        return self.type_movement

    def save(self, *args, **kwargs):
        if self.initial_date > self.finish_date:
            return ValidationError('Data inicial não pode ser maior que data final.')
        return super(Movement, self).save(*args, **kwargs)
