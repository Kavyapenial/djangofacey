from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    hotel = models.ForeignKey(HotelDetail, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    indate = models.DateField(default=0)
    outdate = models.DateField(default=0)