from django.shortcuts import render
from django.urls import reverse
from django.views import generic as views

from Petstagram.common.models import PhotoLike
from Petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
from Petstagram.photos.models import PetPhoto


# def create_photo(request):
#     context = {}
#
#     return render(request, "photos/photo-add-page.html", context)


class PetPhotoCreateView(views.CreateView):
    form_class = PetPhotoCreateForm
    template_name = "photos/photo-add-page.html"
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")

    def get_success_url(self):
        return reverse("details_photo", kwargs={
            "pk": self.object.pk,
        })


# def details_photo(request, pk):
#     context = {
#         "pet_photo": PetPhoto.objects.get(pk=pk)
#     }
#
#     return render(request, "photos/photo-details-page.html", context)

class PetPhotoDetailView(views.DetailView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("photolike_set") \
        .prefetch_related("photocomment_set") \
        .prefetch_related("pets")
    template_name = "photos/photo-details-page.html"


# def edit_photo(request, pk):
#     context = {}
#
#     return render(request, "photos/photo-edit-page.html", context)


class PetPhotoEditView(views.UpdateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")
    template_name = "photos/photo-edit-page.html"
    form_class = PetPhotoEditForm

    def get_success_url(self):
        return reverse("details photo", kwargs={
            "pk": self.object.pk,
        })
