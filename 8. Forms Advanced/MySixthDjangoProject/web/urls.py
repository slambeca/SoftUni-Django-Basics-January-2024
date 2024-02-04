from django.urls import path

from MySixthDjangoProject.web.views import index

urlpatterns = (
    path("", index, name="index"),
)