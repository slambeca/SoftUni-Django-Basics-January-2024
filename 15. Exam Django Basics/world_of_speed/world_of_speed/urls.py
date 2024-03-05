from django.contrib import admin
from django.urls import path, include

from world_of_speed.cars.views import index

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('car/', include('world_of_speed.cars.urls')),
    path('profile/', include('world_of_speed.profiles.urls')),
]
