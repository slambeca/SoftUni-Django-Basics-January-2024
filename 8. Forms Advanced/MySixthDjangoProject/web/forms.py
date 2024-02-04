from django import forms
from django.forms import modelform_factory

from MySixthDjangoProject.web.models import Person


class ReadonlyFieldsMixin:
    def _mark_readonly_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs["readonly"] = "readonly"


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

        labels = {
            "first_name": "First Name:",
        }

        error_message = {
            "first_name": {
                "unique": "The name is not unique!",
            }
        }


class UpdatePersonForm(ReadonlyFieldsMixin, PersonForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields["age"].widget.attrs["readonly"] = "readonly"
        self._mark_readonly_fields()


class NewUpdatePersonForm(ReadonlyFieldsMixin, PersonForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._mark_readonly_fields()


NewPersonForm = modelform_factory(Person, fields="__all__")