from django.urls import path

from ExamPreparationThree.profiles.views import create_profile, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('create/', create_profile, name='create_profile'),
    path('details/', details_profile, name='details_profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('delete/', delete_profile, name='delete_profile'),
)