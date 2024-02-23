from django import forms

from ExamPreparationFour.albums.models import Album
from ExamPreparationFour.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': "Username",
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': "Email",
                }
            ),

            'age': forms.NumberInput(
                attrs={
                    'placeholder': "Age",
                }
            ),
        }


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner', )


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner', )


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner', )