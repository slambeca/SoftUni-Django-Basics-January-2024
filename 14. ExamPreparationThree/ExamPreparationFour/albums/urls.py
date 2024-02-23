from django.urls import path

from ExamPreparationFour.albums.views import create_album, details_album, edit_album, delete_album

urlpatterns = (
    path('add/', create_album, name='create_album'),
    path('<int:album_id>/details/', details_album, name='details_album'),
    path('<int:album_id>/edit/', edit_album, name='edit_album'),
    path('<int:album_id>/delete/', delete_album, name='delete_album'),
)