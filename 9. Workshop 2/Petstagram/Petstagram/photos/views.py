from django.shortcuts import render

from Petstagram.photos.models import PetPhoto


def create_photo(request):
    context = {}

    return render(request, "photos/photo-add-page.html", context)


def details_photo(request, pk):
    context = {
        "pet_photo": PetPhoto.objects.get(pk=pk)
    }

    return render(request, "photos/photo-details-page.html", context)


def edit_photo(request, pk):
    context = {}

    return render(request, "photos/photo-edit-page.html", context)