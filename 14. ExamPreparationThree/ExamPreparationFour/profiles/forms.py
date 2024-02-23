from django import forms

from ExamPreparationFour.profiles.models import Profile


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()