from django.db.models.signals import post_save
from django.dispatch import receiver
from rolepermissions.roles import assign_role

from .models import Account


@receiver(post_save, sender=Account)
def setPermissions(sender, instance, created, **kwargs):
    if created:
        if instance.job == 'D':
            assign_role(instance, 'desenvolvedor')
        elif instance.job == 'G':
            assign_role(instance, 'gerente')
        elif instance.job == 'V':
            assign_role(instance, 'vendedor')
