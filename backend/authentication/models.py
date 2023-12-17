
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    last_login = models.DateTimeField(_("last login"), default=timezone.now)
    profile_picture = models.ImageField(upload_to=f'avatar/{email}', null=True, verbose_name='Фото')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'profile_picture']

    def __str__(self):
        return self.email
