from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from authentication.models import User
from sold_system.models import FurCoatSale, GlovesSale, BagSale, HatSale


@receiver(post_save, sender=User, dispatch_uid="add_permissions")
def update_stock(sender: User, instance: User, created: bool, **kwargs):
    if created:
        all_permissions = Permission.objects.filter(content_type__app_label='sold_system')
        print(all_permissions)
        if all_permissions.exists():
            for permission in all_permissions:
                instance.user_permissions.add(permission)
            instance.save()

        subject = 'Добро пожаловать!'
        message = f'Приветствуем Вас в системе "AbobaCRM"! Ваш логин - {instance.email}, пароль назовет администратор'

        send_mail(subject, message, settings.EMAIL_HOST_USER, [instance.email])
