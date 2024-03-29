from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from Petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from Petstagram.pets.models import Pet
from django.views import generic as views


# def create_pet(request):
#     pet_form = PetCreateForm(request.POST or None)
#     # We can change the PetCreateForm with PetBaseForm
#
#     if request.method == "POST":
#         if pet_form.is_valid():
#             created_pet = pet_form.save()
#             return redirect("details pet", username="Doncho", pet_slug=created_pet.slug)
#
#     context = {
#         "pet_form": pet_form,
#     }
#
#     return render(request, "pets/pet-add-page.html", context)


class PetCreateView(views.CreateView):
    # "model" and "fields" in "CreateView" are only needed to create a form with "modelform_factory"
    # model = Pet
    # fields = ("name", "date_of_birth", "pet_photo")
    form_class = PetCreateForm
    template_name = "pets/pet-add-page.html"

    def get_success_url(self):
        return reverse("details pet", kwargs={
            "username": "Doncho",
            "pet_slug": self.object.slug,
        })


# def details_pet(request, username, pet_slug):
#     context = {
#         "pet": Pet.objects.get(slug=pet_slug)
#     }
#
#     return render(request, "pets/pet-details-page.html", context)


class PetDetailView(views.DetailView):
    # model = Pet  # or "queryset"
    queryset = ((Pet.objects.all().prefetch_related("petphoto_set")
                .prefetch_related("petphoto_set__photolike_set"))
                .prefetch_related("petphoto_set__pets"))
    template_name = "pets/pet-details-page.html"
    # slug_field = "pet_slug" # name of field in Model
    slug_url_kwarg = "pet_slug"  # name of param in URL


# def delete_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     pet_form = PetDeleteForm(request.POST or None, instance=pet)
#
#     if request.method == "POST":
#         pet_form.save()
#         return redirect("index")
#
#     context = {
#         "pet_form": pet_form,
#         "username": username,
#         "pet": pet,
#     }
#
#     return render(request, "pets/pet-delete-page.html", context)


class PetDeleteView(views.DeleteView):
    model = Pet
    form_class = PetDeleteForm

    template_name = "pets/pet-delete-page.html"

    slug_url_kwarg = "pet_slug"

    success_url = reverse_lazy("index")

    extra_context = {
        "username": "Doncho",
    }

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["instance"] = self.object
    #     return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = self.form_class(instance=self.object)

        context["form"] = form

        return context


    # def get_success_url(self):
    #     return reverse("index")    # This is a static url


# def edit_pet(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug).get()
#
#     pet_form = PetEditForm(request.POST or None, instance=pet)
#
#     if request.method == "POST":
#         if pet_form.is_valid():
#             pet_form.save()
#             return redirect('details pet', username=username, pet_slug=pet_slug)
#
#     context = {
#         "pet_form": pet_form,
#         "username": username,
#         "pet": pet,
#     }
#
#     return render(request, "pets/pet-edit-page.html", context)


class PetEditView(views.UpdateView):
    model = Pet  # or "queryset = Pet.objects.all()"
    form_class = PetEditForm
    template_name = "pets/pet-edit-page.html"

    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["username"] = "Doncho"

        return context

    def get_success_url(self):
        return reverse("details pet", kwargs={
            "username": self.request.GET.get("username"),
            "pet_slug": self.object.slug,
        })