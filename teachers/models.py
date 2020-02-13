from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

# Create your models here.


class Teacher(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, default=None)
    pic = models.ImageField(default=None)
    designation = models.CharField(max_length=50, default=None)
    email = models.EmailField(max_length=50, default=None)

    def __str__(self):
        return self.name


def save_teacher(sender, instance, *args, **kwargs):
    
    if instance._state.adding:
        password = get_random_string()
        user = User.objects.create_user(username=instance.email, email=instance.email, password=password, first_name=instance.name)
        user.save()
        instance.user = user

pre_save.connect(save_teacher, sender=Teacher)