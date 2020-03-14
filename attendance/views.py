from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import json
import datetime

from .models import Student, Attendance, AttendanceCaptureProof
from college.models import Batch, Subject
from .serializers import StudentSerializers, AttendanceSerializers, AttendanceCaptureProofSerializers

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.IsAuthenticated]


class AttendanceCaptureProofCreateView(generics.CreateAPIView):
    queryset = AttendanceCaptureProof.objects.all()
    serializer_class = AttendanceCaptureProofSerializers
    permission_classes = [permissions.AllowAny]

class AttendanceConfirmAPIView(views.APIView):
    
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        hour =  request.data['hour']
        subject =  request.data['subject']
        batch = request.data['batch']
        date = datetime.datetime.now()
        student_ids = json.loads(request.data['student_ids']) 
        subjectObj =  Subject.objects.get(pk = subject)

        students = Student.objects.filter(batch = batch)
        for student in students:
            if student.id in student_ids:
                attendance = Attendance(subject = subjectObj, student = student, date = date, hour = hour, is_present = True)
                attendance.save()
            else:
                attendance = Attendance(subject = subjectObj, student = student, date = date, hour = hour, is_present = False)
                attendance.save()
        context = {}
        context['success'] =  True
        return Response(context)