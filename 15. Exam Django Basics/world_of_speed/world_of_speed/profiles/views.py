from django.shortcuts import render, redirect

from world_of_speed.cars.models import Car
from world_of_speed.core.utils import get_profile
from world_of_speed.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm


def create_profile(request):
    profile = get_profile()
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    total_sum = sum(Car.objects.filter(owner=profile).values_list('price', flat=True))

    context = {
        'profile': profile,
        'total_sum': total_sum,
    }

    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()

    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('details_profile')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    form = DeleteProfileForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context)