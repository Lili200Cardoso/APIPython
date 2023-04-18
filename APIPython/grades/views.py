from django.http import HttpResponse 
from APIPython.grades.models import Student
from django.http import JsonResponse
from APIPython.grades.serializers import StudentSerializer
from rest_framework import viewsets

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


