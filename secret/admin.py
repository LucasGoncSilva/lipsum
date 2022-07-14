from django.contrib import admin

from .models import Card, LoginCredential, SecurityNote


# Register your models here.
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('bank', 'name')}

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(LoginCredential)
class LoginCredentialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('service', 'name')}

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(SecurityNote)
class SecurityNoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    def has_change_permission(self, request, obj=None):
        return False
