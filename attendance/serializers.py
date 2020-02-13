from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import api_settings
from rest_framework.response import Response

from .models import Attendance, AttendanceCaptureProof, Student


class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class AttendanceCaptureProofSerializers(serializers.ModelSerializer):
    class Meta:
        model = AttendanceCaptureProof
        fields = '__all__'