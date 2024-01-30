from django.http import HttpResponse
from django.shortcuts import render

from MyRacingClub.members.models import Member


def say_hello_to_members(request):
    my_members = Member.objects.all().order_by("first_name").values()
    context = {
        "my_members": my_members,
    }
    return render(request, "members/show_all_members.html", context)


def details(request, id):
    my_member = Member.objects.get(id=id)
    context = {
        "my_member": my_member
    }
    return render(request, "members/details.html", context)


def main_page(request):
    return render(request, "members/main_page.html")