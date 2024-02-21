from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('ExamPreparation.web.urls')),
    path('album/', include('ExamPreparation.albums.urls')),
    path('profile/', include('ExamPreparation.profiles.urls')),
]
