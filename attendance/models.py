from django.db import models
from user_auth.models import Teacher
# Create your models here.


class Branch(models.Model):
    bname = models.CharField(max_length=50, default=None)
    bcode = models.CharField(max_length=50, default=None)
    
    def __str__(self):
        return self.bname


class Batch(models.Model):
    batch = models.IntegerField(default=0)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    sem = models.IntegerField(default=0)

    def __str__(self):
        return str(self.batch + ' ' + self.branch)


class Student(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    reg_id = models.IntegerField(default=0)
    profile = models.ImageField(default=None)
    name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name


class Subject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subject_code = models.CharField(default='', max_length=6)
    sem = models.IntegerField(default=0)
    subject = models.CharField(max_length=50, default=None)
    credit = models.IntegerField(default=0)
    def __str__(self):
        return self.bname


class Attendance(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=0)
    hour = models.IntegerField(default=0)
    is_present = models.BooleanField(default=False)
