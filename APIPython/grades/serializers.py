from rest_framework import serializers
from APIPython.grades.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student()
        # Você passará somente os fields que vc quer que apareça:
        fields = ["first_name", "last_name"]