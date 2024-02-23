from django.shortcuts import render, redirect

from ExamPreparationFour.albums.views import get_profile
from ExamPreparationFour.profiles.forms import DeleteProfileForm


def details_profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile-details.html', context)


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