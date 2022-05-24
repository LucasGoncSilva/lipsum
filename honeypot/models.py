from django.db import models


# Create your models here.
class Attempt(models.Model):
    IP = models.CharField(max_length=64)
    username = models.CharField(max_length=64, verbose_name='Nome de Usuário')
    password = models.CharField(max_length=64, verbose_name='Senha')
    url = models.CharField(max_length=64)
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data e Horário'
    )

    def __str__(self) -> str:
        date = self.timestamp
        return f'Tentativa {self.pk}: {date.day}/{date.month}/{date.year} ({date.hour}h{date.minute}\'{date.second}\") UTC+3'
