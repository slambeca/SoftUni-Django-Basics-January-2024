from django.urls import path

from MyThirdDjangoProject.employees.views import index

urlpatterns = (
    path("", index, name="index"),
)