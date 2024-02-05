from django import forms
from django.forms import modelform_factory, modelformset_factory

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

    def __init__(self, *args, **kwargs):
        if "user" in kwargs:
            self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data

    # def clean_first_name(self):
    #     pass

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user.is_authenticated:
            instance.created_by = self.user
        instance.save()
        return instance


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

PersonFormSet = modelformset_factory(Person, form=PersonForm, extra=2)
