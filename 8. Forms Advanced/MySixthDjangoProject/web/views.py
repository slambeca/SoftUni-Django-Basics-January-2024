from django.shortcuts import render

from MySixthDjangoProject.web.forms import PersonForm, UpdatePersonForm, NewUpdatePersonForm


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