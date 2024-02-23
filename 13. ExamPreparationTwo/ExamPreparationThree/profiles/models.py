from django.core.validators import MinLengthValidator
from django.db import models

from ExamPreparationThree.common.validators import validate_name


class Profile(models.Model):
    MAX_FIRSTNAME_LENGTH = 25
    MIN_FIRSTNAME_LENGTH = 2

    MAX_LASTNAME_LENGTH = 35
    MIN_LASTNAME_LENGTH = 1

    MAX_EMAIL_LENGTH = 40

    MAX_PASSWORD_LENGTH = 20
    MIN_PASSWORD_LENGTH = 8

    DEFAULT_AGE = 18

    first_name = models.CharField(
        max_length=MAX_FIRSTNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_FIRSTNAME_LENGTH),
            validate_name,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LASTNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_LASTNAME_LENGTH),
            validate_name,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        null=False,
        blank=False,
        unique=True,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        validators=(
            MinLengthValidator(MIN_PASSWORD_LENGTH),
        ),
        null=False,
        blank=False,
        help_text='*Password length requirements: 8 to 20 characters',
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=DEFAULT_AGE,
    )