from django.shortcuts import render, redirect

from ExamPreparationFour.albums.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from ExamPreparationFour.albums.models import Album
from ExamPreparationFour.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    context = {
        'albums': Album.objects.all(),
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def create_album(request):
    profile = get_profile()

    form = CreateAlbumForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.instance.owner = profile
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'albums/album-add.html', context)


def details_album(request, album_id):
    profile = get_profile()
    album = Album.objects.get(id=album_id)

    context = {
        'profile': profile,
        'album': album,
    }

    return render(request, 'albums/album-details.html', context)


def edit_album(request, album_id):
    profile = get_profile()
    album = Album.objects.get(id=album_id)

    form = EditAlbumForm(instance=album)

    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'album': album,
        'form': form,
    }

    return render(request, 'albums/album-edit.html', context)


def delete_album(request, album_id):
    profile = get_profile()
    album = Album.objects.get(id=album_id)

    form = DeleteAlbumForm(instance=album)

    if request.method == 'POST':
        album.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
        'album': album,
    }

    return render(request, 'albums/album-delete.html', context)
