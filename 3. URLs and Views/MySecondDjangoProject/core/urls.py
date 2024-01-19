from django.urls import path

from MySecondDjangoProject.core.views import index, redirect_to_softuni, redirect_to_index

urlpatterns = (
    path("to-softuni/", redirect_to_softuni),
    path("", redirect_to_index, name="blablabla"),
    path("", index),
    path("<int:pk>/", index),
    path("<slug:slug>/", index),
    path("<int:pk>/<slug:slug>/", index),
)