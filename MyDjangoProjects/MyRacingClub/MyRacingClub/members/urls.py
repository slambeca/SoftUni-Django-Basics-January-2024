from django.urls import path

from MyRacingClub.members.views import say_hello_to_members, details, main_page

urlpatterns = (
    path("", main_page, name="main page"),
    path("members/", say_hello_to_members, name="say hello to members"),
    path("members/details/<int:id>", details, name="details"),
)