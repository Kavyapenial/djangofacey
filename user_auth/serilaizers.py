from django.core.validators import validate_email
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response

from .models import Teacher

class TeacherEmailSerializer(serializers.Serializer):

    email = serializers.EmailField(required = True)
    name = serializers.CharField(read_only=True)
    designation= serializers.CharField(read_only=True)
    user =  serializers.IntegerField(read_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs['email']
        teacher = Teacher.objects.filter(email=email)
        if not teacher.exists():
            raise serializers.ValidationError("Teacher does not exist")
        if validate_email(email):
            raise serializers.ValidationError("Please check the email")
        return attrs


    def create(self, validated_data):
        email = validated_data['email']
        teacher = Teacher.objects.get(email=email)
        # following are rest jwt settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(teacher)
        token = jwt_encode_handler(payload)
        token = "JWT " + token
        validated_data['token'] = token
        validated_data['name'] = teacher.name
        validated_data['designation']=teacher.designation
        validated_data['user']=teacher.user.id
        return validated_data