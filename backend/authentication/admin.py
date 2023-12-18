from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class Admin(UserAdmin):
    form = UserChangeForm
    model = User

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'username', 'password1', 'password2'),
            },
        ),
    )


admin.site.register(User, Admin)
