from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import api_settings
from rest_framework.response import Response

from .models import Batch,Branch,Semester, Subject 


class SemesterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Branch
        fields ='__all__'

class BatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields =  '__all__'

class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Semester
        fields = '__all__'