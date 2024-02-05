from django.shortcuts import render

from MySixthDjangoProject.web.forms import PersonForm, UpdatePersonForm, NewUpdatePersonForm, PersonFormSet


def index(request):
    person_form = PersonForm()
    update_person_form = UpdatePersonForm()
    new_update_person_form = NewUpdatePersonForm()

    context = {
        "person_form": person_form,
        "update_person_form": update_person_form,
        "new_update_person_form": new_update_person_form,
    }

    return render(request, "web/index.html", context)


def create_person(request):
    form = PersonForm(request.POST, user=request.user)

    if form.is_valid():
        form.save()


def show_formsets(request):
    form_set = PersonFormSet()
    context = {
        "form_set": form_set
    }

    return render(request, "web/formsets.html", context)