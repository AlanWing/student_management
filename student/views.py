from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from student.models import Student
from student.serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["^name"]
    ordering_fields = ["id"]
