from django.urls import path

from Petstagram.photos.views import create_photo, details_photo, edit_photo


urlpatterns = (
    path("create/", create_photo, name="create photo"),
    path("<int:pk>/", details_photo, name="details photo"),
    path("<int:pk>/edit/", edit_photo, name="edit photo"),
)