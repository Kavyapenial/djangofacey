from django.db import models
from teachers.models import Teacher

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=50, default=None)
    code = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=120, default= None)

    def __str__(self):
        return self.name

class Batch(models.Model):
    year = models.IntegerField(default=0)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    sem = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.batch)


class Subject(models.Model):
    subject_code = models.CharField(default='', max_length=6)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    sem =models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, default=None)
    credit = models.IntegerField(default=0)

    def __str__(self):
        return self.subject
