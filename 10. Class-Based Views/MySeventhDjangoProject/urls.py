from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('MySeventhDjangoProject.web.urls')),
    path("custom/", include('MySeventhDjangoProject.custom_class_base_views.urls')),
]
