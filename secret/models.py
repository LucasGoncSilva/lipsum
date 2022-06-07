from .month.models import MonthField
from django.db import models
from django.urls import reverse

from accounts.models import User


# Create your models here.
class LoginCredential(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credentials', verbose_name='Dono')
    service = models.CharField(max_length=64, verbose_name='Serviço')
    name = models.CharField(max_length=40, verbose_name='Apelido (ex: Conta Principal, Conta de Teste, Compartilhada)')
    thirdy_party_login = models.BooleanField(verbose_name='Login com serviço de terceiro?')
    thirdy_party_login_name = models.CharField(max_length=40, verbose_name='Apelido do serviço de terceiro')
    login = models.CharField(max_length=200, verbose_name='Login')
    password = models.CharField(max_length=200, verbose_name='Senha')
    note = models.TextField(max_length=128, blank=True, null=True, verbose_name='Anotação particular')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.owner.first_name)} | {self.service} | {self.name}'

    def get_absolute_url(self) -> object:
        return reverse('secret:credential_detail_view', args=(str(self.id)))

    class Meta:
        ordering = ['-created']


class Card(models.Model):
    cards_choices = [
        ('Débito', 'Débito'),
        ('Crédito', 'Crédito'),
        ('Pré-pago', 'Pré-pago'),
        ('Co-branded', 'Co-branded'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards', verbose_name='Dono')
    name = models.CharField(max_length=40, verbose_name='Apelido (ex: Cartão da Família, Cartão de Milhas)')
    model = models.CharField(max_length=16, choices=cards_choices, verbose_name='Tipo (débito, crédito, ...)')
    number = models.CharField(max_length=19, verbose_name='Número do Cartão')
    expiration = MonthField(verbose_name='Data de Expiração')
    cvv = models.CharField(max_length=4, verbose_name='cvv')
    bank = models.CharField(max_length=64, verbose_name='Banco')
    brand = models.CharField(max_length=64, verbose_name='Bandeira')
    owners_name = models.CharField(max_length=64, verbose_name='Nome do Contratante (como no cartão)')
    note = models.TextField(max_length=128, blank=True, null=True, verbose_name='Anotação Particular')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.owner.first_name)} | {self.model} | {self.name}'

    def get_absolute_url(self) -> object:
        return reverse('secret:card_detail_view', args=(str(self.id)))

    class Meta:
        ordering = ['-created']


class SecurityNote(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=40)
    content = models.TextField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.owner.first_name)} | {self.name}'

    def get_absolute_url(self) -> object:
        return reverse('secret:note_detail_view', args=(str(self.id)))

    class Meta:
        ordering = ['-created']
