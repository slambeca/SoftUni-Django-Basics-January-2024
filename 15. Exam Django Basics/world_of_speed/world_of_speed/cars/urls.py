from django.urls import path, include

from world_of_speed.cars.views import create_car, catalogue, details_car, edit_car, delete_car

urlpatterns = (
    path('create/', create_car, name='create_car'),
    path('catalogue/', catalogue, name='catalogue'),
    path('<int:car_id>/', include([
        path('details/', details_car, name='details_car'),
        path('edit/', edit_car, name='edit_car'),
        path('delete/', delete_car, name='delete_car'),]
    ))
)