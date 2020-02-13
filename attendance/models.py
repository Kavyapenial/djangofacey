from django.db import models
from college.models import Batch, Subject

from .tasks import get_encodings_from_profile_pic,identify_students_in_pic
from django.db.models.signals import pre_save

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, default=None)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    reg_id = models.IntegerField(default=0)
    profile = models.ImageField(default=None)
    face_encodings = models.BinaryField(null=True)

    def __str__(self):
        return self.name

def save_student(sender, instance, *args, **kwargs):
    instance.face_encodings = get_encodings_from_profile_pic(instance.profile)
    print(instance.face_encodings)

pre_save.connect(save_student, sender=Student)


class Attendance(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=0)
    hour = models.IntegerField(default=0)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)

class AttendanceCaptureProof(models.Model):
    date = models.DateField(default=None)
    capture_image = models.ImageField(default=None)


# def save_image(sender, instance, *args, **kwargs):
#     students = Student.objects.filter(batch = 2)
#     student_ids = identify_students_in_pic(students, instance.capture_image)


# pre_save.connect(save_image, sender=AttendanceCaptureProof)

