from django.urls import path, include

from ExamPreparationThree.fruits.views import add_fruit, details_fruit, edit_fruit, delete_fruit

urlpatterns = (
    path('create/', add_fruit, name='add_fruit'),
    path('<int:fruit_id>', include(
        [
            path('details/', details_fruit, name='details_fruit'),
            path('edit/', edit_fruit, name='edit_fruit'),
            path('delete/', delete_fruit, name='delete_fruit'),
        ])
    )
)