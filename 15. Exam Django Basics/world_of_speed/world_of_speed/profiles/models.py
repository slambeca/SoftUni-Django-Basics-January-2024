from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
from django.db import models


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 3

    MIN_AGE = 21

    MAX_PASS_LENGTH = 20

    MAX_NAME_LENGTH = 25

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH, message='Username must be at least 3 chars long!'),
            RegexValidator(
                regex='^[a-zA-Z0-9_]+$',
                message="Username must contain only letters, digits, and underscores!"),
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(MIN_AGE),
        ),
        # help_text='Age requirement: 21 years and above.',
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_PASS_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True,
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )
