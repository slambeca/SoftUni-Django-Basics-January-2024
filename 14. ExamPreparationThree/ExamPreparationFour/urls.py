from django.contrib import admin
from django.urls import path, include

from ExamPreparationFour.albums.views import index, create_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('create-profile/', create_profile, name='create_profile'),
    path('album/', include('ExamPreparationFour.albums.urls')),
    path('profile/', include('ExamPreparationFour.profiles.urls')),
]
