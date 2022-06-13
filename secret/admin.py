from django.contrib import admin

from .models import Card, LoginCredential, SecurityNote


# Register your models here.
admin.site.register(Card)
admin.site.register(SecurityNote)


@admin.register(LoginCredential)
class LoginCredentialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('service', 'name')}