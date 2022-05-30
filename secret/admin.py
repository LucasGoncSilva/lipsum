from django.contrib import admin

from .models import Card, LoginCredential, SecurityNote


# Register your models here.
admin.site.register(Card)
admin.site.register(LoginCredential)
admin.site.register(SecurityNote)
