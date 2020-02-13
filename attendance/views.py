from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from .models import Student, Attendance, AttendanceCaptureProof
from .serializers import StudentSerializers, AttendanceSerializers, AttendanceCaptureProofSerializers

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.IsAuthenticated]


class AttendanceCaptureProofCreateView(generics.CreateAPIView):
    queryset = AttendanceCaptureProof.objects.all()
    serializer_class = AttendanceCaptureProofSerializers
    permission_classes = [permissions.IsAuthenticated]
