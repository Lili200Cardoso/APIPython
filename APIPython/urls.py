from django.contrib import admin
from django.urls import path, include
from APIPython.grades.views import StudentsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('grades', StudentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
