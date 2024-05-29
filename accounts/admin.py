from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserAdminCreationForm, UserAdminForm

class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
        ('Informaciones Basicas: ', {
            'fields': ('name', 'last_login')
        }),
        ('Permisos: ', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'user_permissions'
            )
        }),
    )
    list_display = ['username', 'email', 'is_active', 'is_staff', 'date_joined']


admin.site.register(User, UserAdmin)
