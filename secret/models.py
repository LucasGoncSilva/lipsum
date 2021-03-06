from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.validators import MinLengthValidator

from account.models import User
from .month.models import MonthField
from .xor_db import xor
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
        verbose_name='Apelido (ex: Conta Principal)'
    )
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
    slug: object = models.SlugField(max_length=128)
    created: object = models.DateTimeField(auto_now_add=True)
    updated: object = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.owner.first_name)} | {self.service} | {self.name}'

    def get_absolute_url(self) -> str:
        return reverse('secret:credential_list_view')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.thirdy_party_login_name = xor(self.thirdy_party_login_name, self.owner.password[21:])
        self.login = xor(self.login, self.owner.password[21:])
        self.password = xor(self.password, self.owner.password[21:])
        self.note = xor(self.note, self.owner.password[21:])

        return super(LoginCredential, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    @classmethod
    def from_db(cls, db, field_names, values):
        cred = super().from_db(db, field_names, values)

        cred.thirdy_party_login_name = xor(cred.thirdy_party_login_name, cred.owner.password[21:], encrypt=False)
        cred.login = xor(cred.login, cred.owner.password[21:], encrypt=False)
        cred.password = xor(cred.password, cred.owner.password[21:], encrypt=False)
        cred.note = xor(cred.note, cred.owner.password[21:], encrypt=False)

        return cred

    def expected_max_length(self, var: str) -> int:
        max_length = {
            'service': 64,
            'name': 40,
            'slug': 128,
            'thirdy_party_login_name': 40,
            'login': 200,
            'password': 200,
        }

        return max_length[var]

    def check_field_length(self, var: str) -> bool:
        value = self.__getattribute__(var)

        return len(value) <= self.expected_max_length(var)

    def all_fields_of_right_length(self) -> bool:
        vars = [
            'service',
            'name',
            'slug',
            'thirdy_party_login_name',
            'login',
            'password',
        ]

        return all(map(self.check_field_length, vars))

    def all_fields_present(self) -> bool:
        if self.owner and self.name \
        and self.service in [slug for slug, _ in credentials_services] \
        and self.slug == f'{self.service}{slugify(self.name)}' \
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
            "<class 'account.models.User'>",
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
        verbose_name='Apelido (ex: Cartão da Família)'
    )
    card_type: object = models.CharField(
        max_length=4,
        choices=cards_types,
        verbose_name='Tipo (débito, crédito, ...)'
    )
    number: object = models.CharField(
        max_length=19,
        validators=[MinLengthValidator(12)],
        verbose_name='Número do Cartão'
    )
    expiration: object = MonthField(verbose_name='Data de Expiração')
    cvv: object = models.CharField(
        max_length=4,
        validators=[MinLengthValidator(3)],
        verbose_name='cvv'
    )
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
    slug: object = models.SlugField(max_length=128)
    created: object = models.DateTimeField(auto_now_add=True)
    updated: object = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.owner.first_name)} | {self.card_type} | {self.name}'

    def get_absolute_url(self) -> str:
        return reverse('secret:card_list_view')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.card_type = xor(self.card_type, self.owner.password[21:])
        self.number = xor(self.number, self.owner.password[21:])
        self.cvv = xor(self.cvv, self.owner.password[21:])
        self.bank = xor(self.bank, self.owner.password[21:])
        self.brand = xor(self.brand, self.owner.password[21:])
        self.owners_name = xor(self.owners_name, self.owner.password[21:])
        self.note = xor(self.note, self.owner.password[21:])

        return super(Card, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    @classmethod
    def from_db(cls, db, field_names, values):
        card = super().from_db(db, field_names, values)

        card.card_type = xor(card.card_type, card.owner.password[21:], encrypt=False)
        card.number = xor(card.number, card.owner.password[21:], encrypt=False)
        card.cvv = xor(card.cvv, card.owner.password[21:], encrypt=False)
        card.bank = xor(card.bank, card.owner.password[21:], encrypt=False)
        card.brand = xor(card.brand, card.owner.password[21:], encrypt=False)
        card.owners_name = xor(card.owners_name, card.owner.password[21:], encrypt=False)
        card.note = xor(card.note, card.owner.password[21:], encrypt=False)

        return card

    def expected_max_length(self, var: str) -> int:
        max_length = {
            'name': 40,
            'card_type': 16,
            'number': 19,
            'cvv': 4,
            'bank': 64,
            'brand': 64,
            'slug': 128,
            'owners_name': 64,
            'note': 128
        }

        return max_length[var]

    def expected_min_length(self, var: str) -> int:
        min_length = {
            'number': 12,
            'cvv': 3,
        }

        return min_length[var]

    def check_field_length(self, var: str) -> bool:
        if var == 'expiration': return True

        value = self.__getattribute__(var)

        if var in ['number', 'cvv']:
            return self.expected_min_length(var) <= len(value) <= self.expected_max_length(var)

        return len(value) <= self.expected_max_length(var)

    def all_fields_of_right_length(self) -> bool:
        vars = [
            'name',
            'card_type',
            'number',
            'expiration',
            'cvv',
            'bank',
            'brand',
            'slug',
            'owners_name',
        ]

        return all(map(self.check_field_length, vars))

    def all_fields_present(self) -> bool:
        return bool(self.owner and self.name \
        and self.card_type in [slug for slug, _ in cards_types] \
        and self.number and self.expiration and self.cvv \
        and self.bank in [slug for slug, _ in cards_banks] \
        and self.brand in [slug for slug, _ in cards_brands] \
        and self.owners_name \
        and self.slug == f'{self.bank}{slugify(self.name)}')

    def all_fields_of_correct_types(self) -> bool:
        if [
            str(type(self.owner)),
            type(self.name),
            type(self.card_type),
            type(self.number),
            str(type(self.expiration)),
            type(self.cvv),
            type(self.bank),
            type(self.brand),
            type(self.slug),
            type(self.owners_name),
        ] == [
            "<class 'account.models.User'>",
            str,
            str,
            str,
            "<class 'secret.month.Month'>",
            str,
            str,
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


class SecurityNote(models.Model):
    owner: object = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name='Dono'
    )
    title: object = models.CharField(max_length=40, verbose_name='Título')
    content: object = models.TextField(max_length=300, verbose_name='Conteúdo')
    slug: object = models.SlugField(max_length=50)
    created: object = models.DateTimeField(auto_now_add=True)
    updated: object = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.owner.first_name)} | {self.title}'

    def get_absolute_url(self) -> str:
        return reverse('secret:note_list_view')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.content = xor(self.content, self.owner.password[21:])

        return super(SecurityNote, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    @classmethod
    def from_db(cls, db, field_names, values):
        note = super().from_db(db, field_names, values)
        note.content = xor(note.content, note.owner.password[21:], encrypt=False)
        return note

    def expected_max_length(self, var: str) -> int:
        max_length = {
            'title': 40,
            'content': 300,
            'slug': 50,
        }

        return max_length[var]

    def check_field_length(self, var: str) -> bool:
        value = self.__getattribute__(var)

        return len(value) <= self.expected_max_length(var)

    def all_fields_of_right_length(self) -> bool:
        vars = [
            'title',
            'content',
            'slug',
        ]

        return all(map(self.check_field_length, vars))

    def all_fields_present(self) -> bool:
        return bool(self.owner and self.title \
        and self.content and self.slug == slugify(self.title))

    def all_fields_of_correct_types(self) -> bool:
        if [
            str(type(self.owner)),
            type(self.title),
            type(self.content),
            type(self.slug),
        ] == [
            "<class 'account.models.User'>",
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
