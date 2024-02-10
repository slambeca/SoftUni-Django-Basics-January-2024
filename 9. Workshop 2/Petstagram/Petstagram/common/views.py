from django.shortcuts import render

from Petstagram.photos.models import PetPhoto


def index(request):
    context = {
        "pet_photos": PetPhoto.objects.all(),
    }

    return render(request, "common/home-page.html", context)