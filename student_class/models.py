from django.db.models import Model
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import DateTimeField


class DateTime(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StudentClass(DateTime):
    grade = CharField(max_length=10, verbose_name="grade")
    sequence_num = IntegerField(verbose_name="sequence number")

    class Meta:
        db_table = "student_class"
