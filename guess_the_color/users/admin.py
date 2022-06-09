from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import UserChangeForm, UserCreationForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser

    list_display = (
        'username', 'email', 'is_staff', 'is_active',
    )
    list_filter = (
        'is_staff', 'is_active'
    )
    fieldsets = (
        (None, {
            'fields': (
                'username', 'email', 'password',
            )
        }),
        ('Права', {
            'fields': (
                'is_staff', 'is_active',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2', 'is_staff',
                'is_active')}
         ),
    )
    search_fields = ('email', )


admin.site.register(CustomUser, CustomUserAdmin)
