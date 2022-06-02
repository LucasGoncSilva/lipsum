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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    name = models.CharField(max_length=40)
    model = models.CharField(max_length=32)
    number = models.CharField(max_length=19)
    expiration = models.DateField()
    cvv = models.CharField(max_length=4)
    bank = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)
    owners_name = models.CharField(max_length=64)
    note = models.TextField(max_length=128, blank=True, null=True)
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
