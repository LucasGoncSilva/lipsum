from django.template.defaultfilters import slugify
from django.db import models

from accounts.models import User
from .month.models import MonthField
from .choices import cards_banks, cards_brands, cards_types, credentials_services


# Create your models here.
class LoginCredential(models.Model):
    owner: object = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='credentials',
        verbose_name='Dono'
    )
    service: object = models.CharField(
        max_length=64,
        choices=credentials_services,
        verbose_name='Serviço'
    )
    name: object = models.CharField(
        max_length=40,
        verbose_name='Apelido (ex: Conta Principal, Conta de Teste, Compartilhada)'
    )
    slug: object = models.SlugField(max_length=128)
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
        return str(self.slug)

    def expected_length(self, var: str) -> int:
        expected_length = {
            'service': 64,
            'name': 40,
            'slug': 128,
            'thirdy_party_login_name': 40,
            'login': 200,
            'password': 200,
        }

        return expected_length[var]


    def check_field_length(self, var: str) -> bool:
        value = self.__getattribute__(var)

        if len(value) <= self.expected_length(var):
            return True
        return False


    def all_fields_of_right_length(self) -> bool:
        vars = [
            'service',
            'name',
            'slug',
            'thirdy_party_login_name',
            'login',
            'password',
        ]

        if all(map(self.check_field_length, vars)):
            return True
        return True

    def all_fields_present(self) -> bool:
        if self.owner and self.service and self.name \
            and self.slug == f'{self.service}-{slugify(self.name)}' \
                and self.thirdy_party_login_name and self.login and self.password:
                if (self.thirdy_party_login == True and self.thirdy_party_login_name != '-----') \
                    or (self.thirdy_party_login != True and self.login != '-----' and self.password != '-----'):
                    return True
        return False

    def all_fields_of_correct_types(self) -> bool:
        if [
            str(type(self.owner)),
            type(self.service),
            type(self.name),
            type(self.slug),
            type(self.thirdy_party_login),
            type(self.thirdy_party_login_name),
            type(self.login),
            type(self.password),
        ] == [
            "<class 'accounts.models.User'>",
            str,
            str,
            str,
            bool,
            str,
            str,
            str,
        ]:
            return True
        return False

    def is_valid(self) -> bool:
        if self.all_fields_present() and self.all_fields_of_correct_types() \
            and self.all_fields_of_right_length():
            return True
        return False

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
    bank: object = models.CharField(
        max_length=64,
        choices=cards_banks,
        verbose_name='Banco'
    )
    brand: object = models.CharField(
        max_length=64,
        choices=cards_brands,
        verbose_name='Bandeira'
    )
    slug: object = models.SlugField(max_length=128, null=True)
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
        return str(self.slug)

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
    slug: object = models.SlugField(max_length=128, null=True)
    content: object = models.TextField(max_length=600, verbose_name='Conteúdo')
    created: object = models.DateTimeField(auto_now_add=True)
    updated: object = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.owner.first_name)} | {self.title}'

    def get_absolute_url(self) -> str:
        return str(self.slug)

    class Meta:
        ordering = ['-created']
