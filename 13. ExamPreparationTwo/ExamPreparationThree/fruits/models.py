from django.core.validators import MinLengthValidator
from django.db import models

from ExamPreparationThree.common.validators import validate_fruit_name
from ExamPreparationThree.profiles.models import Profile


class Fruit(models.Model):
    MAX_FRUITNAME_LENGTH = 30
    MIN_FRUITNAME_LENGTH = 2

    fruit_name = models.CharField(
        max_length=MAX_FRUITNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_FRUITNAME_LENGTH),
            validate_fruit_name,
        ),
        null=False,
        blank=False,
        unique=True,
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.',
        }
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )