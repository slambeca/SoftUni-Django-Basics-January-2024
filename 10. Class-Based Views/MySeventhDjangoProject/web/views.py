from random import random

from django import views
from django.http import HttpResponseNotAllowed
from django.shortcuts import render


def perform_always():
    pass


def index(request):
    perform_always()    # We have to remember to put this function in each of our views

    if request.method == "POST":
        # perform POST logic
        pass
    else:
        # perform GET logic
        pass

    return render(request, "web/index.html")


class BaseView(views.View):
    def dispatch(self, request, *args, **kwargs):
        perform_always()

        return super().dispatch(request, *args, **kwargs)


class IndexView(views.View):
    def dispatch(self, request, *args, **kwargs):
        # check permissions of user
        if random() < 0.5:
            raise HttpResponseNotAllowed(["get"])

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # perform GET logic
        return render(request, "web/index.html")

    def post(self, request):
        # perform POST logic
        return render(request, "web/index.html")