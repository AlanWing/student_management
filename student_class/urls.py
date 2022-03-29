from django.urls import path
from django.urls import include
from rest_framework import routers
from student_class.views import StudentClassViewSet

router = routers.DefaultRouter()
router.register("student_class_resource", StudentClassViewSet, basename="student_class_resource")

urlpatterns = [
    path("", include(router.urls))
]
