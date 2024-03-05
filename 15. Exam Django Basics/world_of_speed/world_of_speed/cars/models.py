from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.profiles.models import Profile


def validate_year(year):
    if not 1999 <= year <= 2030:
        raise ValidationError('Year must be between 1999 and 2030!')


class Car(models.Model):
    CAR_CHOICES = [
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other'),
    ]

    MAX_TYPE_LENGTH = 10

    MAX_MODEL_LENGTH = 15
    MIN_MODEL_LENGTH = 1

    MIN_PRICE = 1.0

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=CAR_CHOICES,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=(
            MinLengthValidator(MIN_MODEL_LENGTH),
        ),
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=(
            validate_year,
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        unique=True,
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        },
        verbose_name='Image URL',
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        ),
        null=False,
        blank=False,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )