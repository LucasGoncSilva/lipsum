from django.contrib import admin

from .models import Card, LoginCredential, SecurityNote


# Register your models here.
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('bank', 'name')}
    list_display = ('pk', 'slug', 'created', 'updated')
    exclude = ('owner', 'card_type', 'number', 'expiration', 'cvv', 'brand', 'owners_name', 'note')

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(LoginCredential)
class LoginCredentialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('service', 'name')}
    list_display = ('pk', 'slug', 'created', 'updated')
    exclude = ('owner', 'thirdy_party_login', 'thirdy_party_login_name', 'login', 'password', 'note')

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(SecurityNote)
class SecurityNoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('pk', 'slug', 'created', 'updated')
    exclude = ('owner', 'content')

    def has_change_permission(self, request, obj=None):
        return False
