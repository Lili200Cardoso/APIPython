from django.contrib import admin
from django.urls import path
from APIPython.grades.views import grades

urlpatterns = [
    path("admin/", admin.site.urls),
    path("grades/", grades)
]
