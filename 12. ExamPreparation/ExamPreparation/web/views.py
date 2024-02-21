from django.shortcuts import render, redirect

from ExamPreparation.albums.models import Album
from ExamPreparation.common.profile_helpers import get_profile
from ExamPreparation.web.forms import CreateProfileForm


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'no_nav': True,
    }

    return render(request, 'web/home-no-profile.html', context)


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)
        # return render(request, 'web/home-no-profile.html')

    context = {
        'albums': Album.objects.all(),
    }

    return render(request, 'web/home-with-profile.html', context)