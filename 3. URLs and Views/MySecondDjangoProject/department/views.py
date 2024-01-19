import time

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(f"Response from {time.time()}")


def department_details(request, pk):
    return HttpResponse(f"Hello from {pk} department!")


def department_by_name(request, name):
    return HttpResponse(f"Hello from {name}. He works in this department.")