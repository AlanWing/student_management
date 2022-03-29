from rest_framework.serializers import ModelSerializer

from student.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        depth = 1
        read_only_fields = ('name',)
