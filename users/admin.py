from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin  as BaseUserAdmin

from .models import User

from .forms import UserCreationForm
# Register your models here.


class UserAdmin(BaseUserAdmin):
    # add_form =  UserCreationForm
    # form =  UserCreationForm

    list_display = ['email', 'first_name', 'last_name', 'is_superuser']
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),

        ('Permissions', {'fields': ('is_superuser',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),

        ('Permissions', {'fields': ('is_superuser',)})
    )

    search_fields =  ('email',)
    ordering = ['email']

    filter_horizontal = ()

admin.site.register(User,UserAdmin)