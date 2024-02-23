from django.contrib import admin
from django.urls import path, include

from ExamPreparationThree.fruits.views import index, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('fruit/', include('ExamPreparationThree.fruits.urls')),
    path('profile/', include('ExamPreparationThree.profiles.urls')),
]
