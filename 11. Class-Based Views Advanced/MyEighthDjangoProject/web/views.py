import json
import random

from django import forms
from django.urls import reverse_lazy
from django.views import generic as views

from MyEighthDjangoProject.web.models import Todo


def create_todo(request):
    pass


# def index(request):
#     context = {
#         "todo_list": [t.title for t in Todo.objects.all()],
#     }
#
#     return HttpResponse(json.dumps(context))


# All of our views should follow one naming convention
# <Action><Entity><View>
class SearchTodoByTitleForm(forms.Form):
    title = forms.CharField(
        max_length=Todo.MAX_TITLE_LENGTH,
        required=False,
    )

    is_done = forms.BooleanField(
        required=False,
    )


class CreateTodoView(views.CreateView):
    model = Todo  # queryset = Todo.objects.all()

    fields = "__all__"  # or exclude or form_class

    template_name = "web/create_todo.html"

    success_url = reverse_lazy("index")


class DetailTodoView(views.DetailView):
    model = Todo
    template_name = "web/detail_todo.html"


class LatestCreatedMixin:
    latest_created_count = 5

    def get_queryset(self):
        return super().get_queryset().order_by("-pk")[:self.latest_created_count]


class ListTodoView(LatestCreatedMixin, views.ListView):
    model = Todo
    latest_created_count = 7
    template_name = "web/list_todo.html"

    # context_object_name = todos  # this is not a good practice

    # Static way
    # paginate_by = 3

    # Dynamic way
    def get_paginate_by(self, queryset=None):
        return random.randint(1, 6)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Todos list"
        # context["object_list"] = context["object_list"].filter(title__icontains="clean")

        context["search_form"] = SearchTodoByTitleForm()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        title_pattern = self.get_title_pattern()

        if title_pattern:
            queryset = queryset.filter(title__icontains=title_pattern)

        # queryset = queryset.filter(title__icontains='clean')

        is_done = self.get_is_done_filter()
        if is_done is not None:
            queryset = queryset.filter(is_done=is_done)

        return queryset

    def get_title_pattern(self):
        return self.request.GET.get("title", None)

    def get_is_done_filter(self):
        return self.request.GET.get("is_done", None) == "no"