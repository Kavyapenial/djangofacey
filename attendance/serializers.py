from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import api_settings
from rest_framework.response import Response

from .models import Attendance, AttendanceCaptureProof, Student, StudentObject
from .tasks import identify_students_in_pic

class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentResultSerailizers(serializers.Serializer):
    id =  serializers.IntegerField()
    name = serializers.CharField()
    batch = serializers.IntegerField()
    reg_id = serializers.IntegerField()
    profile = serializers.CharField()
    is_present = serializers.BooleanField()
    
class AttendanceCaptureProofSerializers(serializers.ModelSerializer):
    students_data = serializers.ListField(read_only = True)
    batch = serializers.IntegerField(write_only = True)
    class Meta:
        model = AttendanceCaptureProof
        fields = ('capture_image', 'students_data','batch')

    def create(self, validated_data):
        students = Student.objects.filter(batch = validated_data['batch'])
        students_result = identify_students_in_pic(students, validated_data['capture_image'], StudentObject)
        student_serializer = StudentResultSerailizers(students_result, many = True)
        validated_data['students_data'] = student_serializer.data
        attendace = AttendanceCaptureProof(date= '2019-03-10', capture_image =  validated_data['capture_image'])
        attendace.save()
        return validated_data

class AttendanceConfirmSerializers(serializers.Serializer):
    student_prescent_id = serializers.ListField()

    def create(self, validated_data):
        print(validated_data['student_prescent_id'])
        return validated_data