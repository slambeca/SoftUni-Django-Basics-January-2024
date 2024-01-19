from django.http import HttpResponse
from django.shortcuts import redirect


def index(request, *args, **kwargs):
    content = f"It works with:<br/>" + \
              f" args={args} and kwargs={kwargs}<br/> " + \
              f"from {request.path}<br/> " + \
              f"using {request.method} method <br/>" + \
              f"and user {request.user}"

    return HttpResponse(
        content,
        status=201,
    )


def redirect_to_softuni(request):
    return redirect("https://softuni.bg")


def redirect_to_index(request):
    return redirect("blablabla")