from django import forms

from MySeventhDjangoProject.web.models import ToDo


class ToDoBaseForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = "__all__"

    def clean_title(self):
        pass

    def save(self, commit=True):
        pass