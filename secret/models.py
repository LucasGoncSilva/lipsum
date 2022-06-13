from .month.models import MonthField
from django.db import models
from django.urls import reverse

from accounts.models import User
from .choices import cards_banks, cards_brands, cards_types, credentials_services


# Create your models here.
class LoginCredential(models.Model):
    owner: object = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='credentials',
        verbose_name='Dono'
    )
    service: object = models.CharField(max_length=64, choices=credentials_services, verbose_name='Serviço')
    name: object = models.CharField(
        max_length=40,
        verbose_name='Apelido (ex: Conta Principal, Conta de Teste, Compartilhada)'
    )
    slug: object = models.SlugField()
    thirdy_party_login: object = models.BooleanField(verbose_name='Login com serviço de terceiro?')
    thirdy_party_login_name: object = models.CharField(
        max_length=40,
        verbose_name='Apelido do serviço de terceiro'
    )
    login: object = models.CharField(max_length=200, verbose_name='Login')
    password: object = models.CharField(max_length=200, verbose_name='Senha')
    note: object = models.TextField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='Anotação particular'
    )
    created: object = models.DateTimeField(auto_now_add=True)
    updated: object = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.owner.first_name)} | {self.service} | {self.name}'

    def get_absolute_url(self) -> str:
        return reverse('secret:credential_detail_view', args=(str(self.slug)))

    class Meta:
        ordering = ['-created']


class Card(models.Model):
    owner: object = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cards',
        verbose_name='Dono'
    )
    name: object = models.CharField(
        max_length=40,
        verbose_name='Apelido (ex: Cartão da Família, Cartão de Milhas)'
    )
    card_type: object = models.CharField(
        max_length=16,
        choices=cards_types,
        verbose_name='Tipo (débito, crédito, ...)'
    )
    number: object = models.CharField(max_length=19, verbose_name='Número do Cartão')
    expiration: object = MonthField(verbose_name='Data de Expiração')
    cvv: object = models.CharField(max_length=4, verbose_name='cvv')
    bank: object = models.CharField(max_length=64, choices=cards_banks,verbose_name='Banco')
    brand: object = models.CharField(max_length=64, choices=cards_brands,verbose_name='Bandeira')
    owners_name: object = models.CharField(
        max_length=64,
        verbose_name='Nome do Titular (como no cartão)'
    )
    note: object = models.TextField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='Anotação Particular'
    )
    created: object = models.DateTimeField(auto_now_add=True)
    updated: object = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.owner.first_name)} | {self.model} | {self.name}'

    def get_absolute_url(self) -> str:
        return reverse('secret:card_detail_view', args=(str(self.id)))

    class Meta:
        ordering = ['-created']


class SecurityNote(models.Model):
    owner: object = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name='Dono'
    )
    title: object = models.CharField(max_length=40, verbose_name='Título')
    content: object = models.TextField(max_length=600, verbose_name='Conteúdo')
    created: object = models.DateTimeField(auto_now_add=True)
    updated: object = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.owner.first_name)} | {self.title}'

    def get_absolute_url(self) -> str:
        return reverse('secret:note_detail_view', args=(str(self.id)))

    class Meta:
        ordering = ['-created']
