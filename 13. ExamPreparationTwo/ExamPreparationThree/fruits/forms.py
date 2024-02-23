from django import forms

from ExamPreparationThree.fruits.models import Fruit


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit

        exclude = ('owner',)

        labels = {
            'fruit_name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fruit_name'].widget.attrs['placeholder'] = 'Fruit Name'
        self.fields['image_url'].widget.attrs['placeholder'] = 'Fruit Image URL'
        self.fields['description'].widget.attrs['placeholder'] = 'Fruit Description'
        self.fields['nutrition'].widget.attrs['placeholder'] = 'Nutrition Info'


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)

    fruit_name = forms.CharField(label='Name')
    image_url = forms.URLField(label='Image URL')


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('fruit_name', 'image_url', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    fruit_name = forms.CharField(label='Name')
    image_url = forms.URLField(label='Image URL')

