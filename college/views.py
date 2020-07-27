from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from .models import Batch, Branch, Semester, Subject
from teachers.models import Teacher
from .serilalizers import BranchSerializers, BatchSerializers, SemesterSerializers, SubjectSerializers

class SubjectListView(generics.ListAPIView):
    queryset =  Subject.objects.all()
    serializer_class = SubjectSerializers
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, id,  *args, **kwargs):
        teacher =  Teacher.objects.filter(user=request.user)
        if teacher.exists():
            queryset = Subject.objects.filter(branch = id,teacher=teacher[0])
        else:
            queryset = Subject.objects.filter(branch = id)
        serializer = SubjectSerializers(queryset, many = True)
        return Response(serializer.data)

class BatchListView(generics.ListAPIView):
    queryset =  Batch.objects.all()
    serializer_class = BatchSerializers
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, id,  *args, **kwargs):
        queryset = Batch.objects.filter(branch = id)
        serializer = BatchSerializers(queryset, many = True)
        return Response(serializer.data)


class BranchListView(generics.ListAPIView):
    queryset =  Branch.objects.all()
    serializer_class = BranchSerializers
    permission_classes = [permissions.IsAuthenticated]

class SemesterListView(generics.ListAPIView):
    queryset =  Semester.objects.all()
    serializer_class = SemesterSerializers
    permission_classes = [permissions.IsAuthenticated]



