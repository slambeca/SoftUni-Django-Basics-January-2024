from django.shortcuts import render

from Petstagram.pets.models import Pet


def create_pet(request):
    context = {}

    return render(request, "pets/pet-add-page.html", context)


def details_pet(request, username, pet_slug):
    context = {
        "pet": Pet.objects.get(slug=pet_slug)
    }

    return render(request, "pets/pet-details-page.html", context)


def delete_pet(request, username, pet_slug):
    context = {}

    return render(request, "pets/pet-delete-page.html", context)


def edit_pet(request, username, pet_slug):
    context = {}

    return render(request, "pets/pet-edit-page.html", context)