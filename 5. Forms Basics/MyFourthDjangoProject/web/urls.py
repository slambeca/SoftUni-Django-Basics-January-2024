from django.urls import path

from MyFourthDjangoProject.web.views import index

urlpatterns = (
    path("", index, name="index"),
)