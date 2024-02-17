from django.urls import path

from MyEighthDjangoProject.web.views import CreateTodoView, ListTodoView, DetailTodoView

urlpatterns = (
    # FBV
    # path("create/", create_todo, name="create todo"),
    path("", ListTodoView.as_view(), name="index"),
    # CBV
    path("create/", CreateTodoView.as_view(), name="create todo view"),    # name="todos_create"
    path("<int:pk>/", DetailTodoView.as_view(), name="todos details"),
)