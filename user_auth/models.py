from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Teacher(models.Model):
    t_id = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default=None)
    pic = models.ImageField(default=None)
    designation = models.CharField(max_length=50, default=None)
    email = models.EmailField(max_length=50, default=None)
