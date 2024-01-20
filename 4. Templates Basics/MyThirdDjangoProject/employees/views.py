from django.shortcuts import render


class Person:
    def __init__(self, first_name, last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


def index(request):
    new_person = Person(
        first_name="Toncho",
        last_name="Moncho",
    )

    context = {
        "title": "Employees list",
        "first_name": "Borislav",
        "last_name": "Ivanov",
        "department": "Quality Assurance",
        "email_address": "borislav@ivanov.com",
        "person": {
            "first_name": "Doncho",
            "last_name": "Minkov"
        },
        "person_obj": Person(
            first_name="Doncho",
            last_name="Minkov"),
        "numbers": [1, 2, 3, 4, 5],
        "names": ["Borislav", "Pesho", "Gosho"],
        "new_person": new_person,
        "new_person_dict": new_person.__dict__,
    }

    return render(request, "employees/index.html", context)
