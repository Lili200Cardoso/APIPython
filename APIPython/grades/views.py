from django.http import HttpResponse 
from APIPython.grades.models import Student
from django.http import JsonResponse
from APIPython.grades.serializers import StudentSerializer

def grades(request):
    if request.method == "GET":
        student = Student.objects.first()
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
