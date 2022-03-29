from django.db.models import Model
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import TextChoices
from django.db.models import ForeignKey
from django.db.models import CASCADE
from django.db.models import Model
from django.db.models import DateTimeField

from student_class.models import StudentClass


class DateTime(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GenderChoices(TextChoices):
    MALE = "M"
    FEMALE = "F"


class Student(DateTime):
    cls = ForeignKey(StudentClass, on_delete=CASCADE, verbose_name="student class", related_name="students")
    name = CharField(max_length=20, verbose_name="student name")
    gender = CharField(max_length=1, choices=GenderChoices.choices, verbose_name="gender")
    age = IntegerField(verbose_name="age")

    class Meta:
        db_table = "student"
