from django.contrib.auth import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Teacher

@receiver(pre_save, sender=Teacher)
def save_teacher(sender, instance, *args, **kwargs):
    if not instance._state.adding:
            print ('this is an update')
    else:
        print ('this is an insert')