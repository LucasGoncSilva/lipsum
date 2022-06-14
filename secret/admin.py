from django.contrib import admin

from .models import Card, LoginCredential, SecurityNote


# Register your models here.
@admin.register(Card)
class Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('bank', 'name')}


@admin.register(LoginCredential)
class LoginCredentialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('service', 'name')}


@admin.register(SecurityNote)
class Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
