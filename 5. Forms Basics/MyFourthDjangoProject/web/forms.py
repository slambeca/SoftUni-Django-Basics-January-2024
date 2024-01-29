from django import forms


class EmployeeForm(forms.Form):
    MAX_FIRST_NAME_LENGTH = 35
    MAX_LAST_NAME_LENGTH = 35

    first_name = forms.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        required=True,    # Instead of blank and null
        label="Type your first name here"
    )

    last_name = forms.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        required=True,
        label="Type your last name here"
    )

    age = forms.IntegerField(
        label="Your age is?"
    )

    password = forms.CharField(
        label="Choose your password carefully!",
        widget=forms.PasswordInput(),
    )

    email = forms.EmailField(
        label="What is your email? I want to send you spam.",
    )

    interests = forms.ChoiceField(
        label="Your interests are?",
        choices=(
            (1, "Gaming"),
            (2, "Reading"),
            (3, "Hiking"),
            (4, "Sport"),
        )
    )

    description = forms.CharField(
        widget=forms.Textarea,
        label="Describe yourself in 100 words:",
    )

    question = forms.CharField(
        label="Are you a programmer?",
        initial="True",
        disabled=True,
    )