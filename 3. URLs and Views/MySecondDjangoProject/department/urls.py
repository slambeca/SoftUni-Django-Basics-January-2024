from django.urls import path

from MySecondDjangoProject.department.views import department_details, department_by_name

urlpatterns = (
    path("department/<int:pk>", department_details),
    path("department/<str:name>", department_by_name),
)

