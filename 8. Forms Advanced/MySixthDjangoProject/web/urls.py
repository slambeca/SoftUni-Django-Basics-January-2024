from django.urls import path

from MySixthDjangoProject.web.views import index, create_person, show_formsets

urlpatterns = (
    path("", index, name="index"),
    path("person/create/", create_person, name="create_person"),
    path("formsets/", show_formsets, name="show_formsets"),
)