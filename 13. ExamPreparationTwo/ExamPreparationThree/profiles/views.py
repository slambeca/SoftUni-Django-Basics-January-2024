from django.shortcuts import render, redirect

from ExamPreparationThree.common.helpers import get_profile
from ExamPreparationThree.fruits.models import Fruit
from ExamPreparationThree.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm


def create_profile(request):
    profile = get_profile()
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    count_fruits = Fruit.objects.filter(owner=profile).count()

    context = {
        'profile': profile,
        'count_fruits': count_fruits,
    }
    return render(request, 'profiles/details-profile.html', context)


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

    return render(request, 'profiles/edit-profile.html', context)


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

    return render(request, 'profiles/delete-profile.html', context)