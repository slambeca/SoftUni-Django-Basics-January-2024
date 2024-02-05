from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_first_name(value):
    if " " in value:
        raise ValidationError("First name cannot contain a whitespace!")


class Person(models.Model):
    # MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 32
    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_LAST_NAME = 32

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            validate_first_name,
            MinLengthValidator(1),  # This is a validator that is basically a class
        )
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_LAST_NAME),
        )
    )

    age = models.PositiveSmallIntegerField()

    # created_by = models.ForeignKey(
    #     User,
    #     on_delete=models.DO_NOTHING,
    #     null=True,
    # )