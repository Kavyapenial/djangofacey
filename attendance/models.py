from django.db import models
from college.models import Batch, Subject
# Create your models here.

class Student(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    reg_id = models.IntegerField(default=0)
    profile = models.ImageField(default=None)
    name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=0)
    hour = models.IntegerField(default=0)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)

