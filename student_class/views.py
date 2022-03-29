from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from student_class.models import StudentClass
from student_class.serializers import StudentClassSerializer


class StudentClassViewSet(viewsets.ViewSet):

    def list(self, request):
        classes = StudentClass.objects.all()
        print(classes)
        class_serializer = StudentClassSerializer(classes, many=True)
        return JsonResponse(class_serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        queryset = StudentClass.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StudentClassSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        data = JSONParser().parse(request)
        print(data)
        student_class_serializer = StudentClassSerializer(data=data)
        if student_class_serializer.is_valid():
            student_class_serializer.save()
            return JsonResponse(student_class_serializer.data, status=201)
        return JsonResponse(student_class_serializer.errors, status=400)

    def destroy(self, request, pk=None):
        cls = StudentClass.objects.get(pk=pk)
        cls.delete()
        return HttpResponse(status=204)

    def update(self, request, pk=None):
        cls = StudentClass.objects.get(pk=pk)
        data = JSONParser().parse(request)
        cls_serializer = StudentClassSerializer(cls, data=data)
        if cls_serializer.is_valid():
            cls_serializer.save()
            return JsonResponse(cls_serializer.data, status=201)
        return JsonResponse(cls_serializer.errors, status=400)
