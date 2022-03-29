from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from student.views import StudentViewSet

router = DefaultRouter()
router.register("student_resource", StudentViewSet, basename="student_resource")

urlpatterns = [
    path("", include(router.urls)),
]
