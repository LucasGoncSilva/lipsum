from django.db import models

from accounts.models import User


# Create your models here.
class LoginCredential(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credentials')
    name = models.CharField(max_length=40)
    service = models.CharField(max_length=64)
    thirdy_party_login = models.BooleanField()
    thirdy_party_login_name = models.CharField(max_length=40, blank=True, null=True)
    login = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(max_length=128, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def get_my_model_name(self):
        return self._meta.model_name

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
        return self.name

    class Meta:
        ordering = ['-created']


class SecurityNote(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=40)
    content = models.TextField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-created']
