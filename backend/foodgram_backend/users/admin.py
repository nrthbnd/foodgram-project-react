from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
    )
    list_editable = (
        'first_name',
        'last_name',
    )
    search_fields = (
        'username',
        'email'
    )
    list_filter = (
        'username',
        'email',
    )
    empty_value_display = '-пусто-'
