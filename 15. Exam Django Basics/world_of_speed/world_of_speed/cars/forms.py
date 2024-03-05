from django import forms

from world_of_speed.cars.models import Car


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car

        exclude = ('owner',)


class CreateCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image_url'].widget.attrs['placeholder'] = 'https://...'


class EditCarForm(BaseCarForm):
    ...


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'