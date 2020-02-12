from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from .serilaizers import TeacherEmailSerializer


class TeacherEmail(object):
    token = None
    def __init__(self, email, token):
        self.email = email
        self.token = token


class TeacherEmailVerify(APIView):
    """
    Teacher email id verification

    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        
        teacherEmailSerializer =  TeacherEmailSerializer(data = request.POST)
        if not teacherEmailSerializer.is_valid():
            return Response(teacherEmailSerializer.errors, 400)
        else:

            teacherObject =  teacherEmailSerializer.save()
            print(teacherEmailSerializer)
            return Response(teacherEmailSerializer.data,200)


# Create your views here.

