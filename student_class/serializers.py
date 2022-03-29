from rest_framework.serializers import Serializer
from rest_framework.serializers import PrimaryKeyRelatedField
from rest_framework.serializers import IntegerField
from rest_framework.serializers import DateTimeField
from rest_framework.serializers import CharField

from student_class.models import StudentClass


class StudentClassSerializer(Serializer):
    id = IntegerField(read_only=True)
    students = PrimaryKeyRelatedField(many=True, read_only=True)
    updated_at = DateTimeField(read_only=True)
    created_at = DateTimeField(read_only=True)
    grade = CharField()
    sequence_num = IntegerField()

    def update(self, instance, validated_data):
        instance.grade = validated_data.get("grade", instance.grade)
        instance.sequence_num = validated_data.get("sequence_num", instance.sequence_num)
        instance.save()
        return instance

    def create(self, validated_data):
        cls = StudentClass(**validated_data)
        cls.save()
        return cls
