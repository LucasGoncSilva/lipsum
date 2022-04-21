from django.contrib import admin

from .models import Attempt


# Register your models here.
@admin.register(Attempt)
class AttempAdmin(admin.ModelAdmin):
    readonly_fields = ('IP', 'username', 'password', 'url', 'timestamp')