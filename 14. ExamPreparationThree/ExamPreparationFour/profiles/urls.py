from django.urls import path

from ExamPreparationFour.profiles.views import details_profile, delete_profile

urlpatterns = (
    path('details/', details_profile, name='details_profile'),
    path('delete/', delete_profile, name='delete_profile'),
)