from django.db import models
from user_auth.models import Teacher
# Create your models here.
class Batch(models.Model):
    branch_id = models.IntegerField(default=0)
    batch = models.IntegerField(default=0)
    branch = models.CharField(max_length=50, default=None)

class Student(models.Model):
    branch_id = models.ForeignKey(Batch, on_delete=models.CASCADE)
    reg_id = models.IntegerField(default=0)
    pic = models.ImageField(default=None)
    name = models.CharField(max_length=50, default=None)

class Subject(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Batch, on_delete=models.CASCADE)
    sub_id = models.IntegerField(default=0)
    sem = models.IntegerField(default=0)
    subject = models.CharField(max_length=50, default=None)
    credit = models.IntegerField(default=0)

class Attendance(models.Model):
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    stud_reg_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=0)
    hour = models.IntegerField(default=0)
    is_present = models.BooleanField(default=False)






   