from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'name', 'surname', 'phone_number', 'skills', 'is_active', 'dark_mode')
    list_filter = ('email', 'name', 'surname', 'phone_number', 'skills', 'is_active', 'dark_mode')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'surname', 'phone_number', 'skills', 'dark_mode')}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'surname', 'phone_number', 'skills',  'is_active',
                       'dark_mode')}
         ),
    )
    search_fields = ('email', 'name', 'surname', 'phone_number', 'skills',)
    ordering = ('email', 'name', 'surname', 'phone_number', 'skills',)
