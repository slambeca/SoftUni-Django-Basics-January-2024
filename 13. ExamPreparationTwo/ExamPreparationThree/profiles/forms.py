from django import forms

from ExamPreparationThree.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ('first_name', 'last_name', 'email', 'password')

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ('first_name', 'last_name', 'image_url', 'age')

    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    image_url = forms.URLField(label='Image URL')
    age = forms.IntegerField(label='Age')


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()